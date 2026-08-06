# 📄 ResumeAI

An AI-powered resume optimization tool built with **Python, Flask, and Google's Gemini API** that rewrites resumes to better match a target job description while remaining truthful.

ResumeAI allows users to upload an existing resume, provide a job description, and generate an ATS-friendly version that emphasizes relevant skills, improves formatting, and preserves factual information. The generated resume can then be downloaded as a Microsoft Word (.docx) document.

---

## ✨ Features

- 📄 Upload resume in PDF format
- 🤖 AI-powered resume optimization using Gemini
- 🎯 Prompt engineered for ATS-friendly output
- 📝 Grammar and formatting improvements
- ⚖️ Truth-preserving resume rewriting (no fabricated experience)
- ❌ Graceful API error handling
- 📥 Download generated resume as a DOCX file
- 🎨 Responsive user interface built with HTML, CSS, and JavaScript

---

## 🛠 Tech Stack

### Backend

- Python
- Flask
- Google Gemini API
- python-docx
- PyPDF
- Werkzeug

### Frontend

- HTML5
- CSS3
- JavaScript

---

## ⚙️ How It Works

1. User uploads a PDF resume.
2. PyPDF extracts the resume text.
3. The user provides a target job description.
4. A carefully engineered prompt is sent to the Gemini API.
5. Gemini rewrites the resume while:
   - preserving factual information
   - improving ATS compatibility
   - prioritizing relevant skills
   - improving grammar and formatting
6. The generated resume is displayed in the browser.
7. The result is saved as a DOCX document and can be downloaded.

---

## 📂 Project Structure

```
ResumeAI/
│
├── static/
│   ├── site.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Prompt Engineering

Instead of simply asking the AI to "improve the resume", ResumeAI uses structured prompting with clearly separated sections:

- **Role**
- **Input**
- **Task**
- **Rules**
- **Output**

The prompt instructs Gemini to:

- remain truthful
- avoid inventing experience
- improve ATS compatibility
- preserve important qualifications
- prioritize relevant skills based on the supplied job description
- return plain text only

This produces more reliable and consistent outputs than a simple prompt.

---

## 🛡 Error Handling

The application gracefully handles Gemini API failures using Python exception handling.

Instead of crashing when the API is unavailable, the application:

- logs the original exception for debugging
- returns a user-friendly error message
- keeps the web application responsive

---

## 💡 What I Learned

Building ResumeAI helped me gain practical experience with:

- Flask routing
- File uploads
- Reading PDF files
- Calling external AI APIs
- Prompt engineering
- Exception handling
- Dynamic HTML rendering with Jinja
- JavaScript DOM manipulation
- Responsive CSS layouts
- DOCX generation

---

## 🚀 Future Improvements

- Support for DOCX resume uploads
- Export as PDF
- Resume scoring
- Dark mode
- Authentication
- Resume version history
- Multiple resume templates

---

## 📸 Screenshot

_Add a screenshot of the application here._

---

## ▶️ Running Locally

Clone the repository:

```bash
git clone https://github.com/yourusername/ResumeAI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 📜 License

This project was built for learning, experimentation, and portfolio purposes.