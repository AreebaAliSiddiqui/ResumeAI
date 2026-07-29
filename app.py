from flask import Flask
from flask import render_template , request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from pypdf import PdfReader
from google import genai
from google.genai import types
from dotenv import load_dotenv
from google.genai import Client
from urllib import response

load_dotenv()

client= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

client=Client()
response_1=client.models.generate_content(
     model=MODEL_ID,
     contents="Hello"


response_2=client.models.generate_content
    model=MODEL_ID
    contents='Ask a question about the text you provided',)


response_1=client.models.generate_content(
     model='gemini-2.5-flash',
     contents='Why is the sky blue'

)
print(response.text)

file = client.files.upload(file='a11.txt')
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=['Could you summarize this file?', file]
)
print(response.text)
client.close()



api_key = os.getenv("GEMINI_API_KEY")

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


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
            # check if the post request has the file part
            if 'resume' not in request.files:
                flash('No file part')
                return redirect(request.url)
            
            file = request.files['resume']
            job_description = request.form.get('job_description', '')
            print(f"Job Description: {job_description}")
            # if user does not select file, browser also
            # submit an empty part without filename

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

        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



