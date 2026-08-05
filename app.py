from flask import Flask
from flask import render_template , request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv
from flask import send_file



load_dotenv()
client= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


app = Flask(__name__)
app.secret_key = 'riva-1111'  # Replace

UPLOAD_FOLDER ='path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ----- Gemini Functions -----

def generate_resume(resume_text, job_description):
    prompt=(  
    f"ROLE:You are a professional, world class resume writer. INPUT: Here is the candidate's resume:\n{resume_text}\n"
    f"And this job description: \n{job_description}\n"
    f"TASK:Rewrite the resume so it better matches the job description for example reorder bullet points,emphasize relevant projects,prioritize matching skills while remaining truthful."
    f"RULES:Don't invent experience. "
    f"Improve ATS compatibility to maximize the candidate's chances of passing an Applicant Tracking System "
    f"Use bullet points. "
    f"Improve grammar. "
    f"Preserve all important experience, education, certifications, and technical skills unless they are clearly irrelevant. "
    f"Match the job description. "
    f"Keep professional tone. "
    f"OUTPUT: Return plain text only."
    )
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt
        )
        return response.text

    except Exception as e:
        print(f"Error generating resume: {e}")
        return "Error generating resume. Please try again later."
       


@app.route('/', methods=['GET', 'POST'])
def index():
        resume = None
        print("=== index() called ===")
        if request.method == 'POST':
            print("=== POST request ===")
            # check if the post request has the file part
            if 'resume' not in request.files:
                flash('No file part')
                return redirect(request.url)
            
            file = request.files['resume']
            job_description = request.form.get('job_description', '')
            print(f"Job Description: {job_description}")
            
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                print(f"File saved to: {file_path}")
                # Read the PDF file
                reader = PdfReader(file_path)
                print(f"Number of pages: {len(reader.pages)}")
                page = reader.pages[0]
                text = page.extract_text()
                print(f"Extracted text: {text}")
            else:
                 print("No valid file uploaded.")

            resume = generate_resume(text, job_description)
            with open('response.txt', 'w', encoding='utf-8') as file:
                file.write(resume)
            
            print(resume)
        return render_template('index.html', resume=resume)

@app.route('/download_resume', methods=['GET'])   
def download_resume():
    return send_file( 
        'response.txt',
         as_attachment=True
        )
if __name__ == '__main__':
    app.run(debug=True)



