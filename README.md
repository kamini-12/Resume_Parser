
# 📝 Resume Parser Web App

A basic Resume Parser web application built using Flask (backend) and React (frontend). It allows users to upload resumes and extract key information using Natural Language Processing (NLP).

## 🔧 Features

- Upload resumes (PDF, DOCX, TXT)
- Extract key details:
  - Name
  - Email
  - Phone Number
  - Skills
  - Work Experience
  - Education
- Match resumes with job descriptions and get an ATS score
- Simple signup and login functionality

## 💻 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: React.js
- **Database**: SQLite / PostgreSQL / MySQL

## 📦 Getting Started

### Backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

## 📁 Project Structure

```
resume-parser/
├── backend/             # Flask backend
├── frontend/            # React frontend
└── README.md
```

## 📃 License

This project is licensed under the MIT License.

---

⭐ Feel free to star the repo if you find it helpful!
```
