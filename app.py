from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
import pdfplumber
import docx
import re

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract details from text
def extract_details(text):
    details = {
        "name": re.search(r"([A-Z][a-z]+\s[A-Z][a-z]+)", text),
        "email": re.search(r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}", text),
        "phone": re.search(r"\b\d{10}\b", text),
        "skills": re.findall(r"\b(?:Python|SQL|Java|Machine Learning|Data Analysis|Excel)\b", text, re.IGNORECASE)
    }

    extracted_details = {
        key: (match.group() if match else "Not Found") if key != "skills" else (details["skills"] if details["skills"] else "Not Found")
        for key, match in details.items()
    }
    return extracted_details

# Route to serve the landing page
@app.route("/")
def landing_page():
    return render_template("Landing.html")

# Route to handle file uploads
@app.route("/upload", methods=["POST"])
def upload():
    if "resume-file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume-file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Save the uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Process the file based on its type
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(filepath)
    elif file.filename.endswith(".docx"):
        text = extract_text_from_docx(filepath)
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    # Extract details from the text
    details = extract_details(text)
    return jsonify(details)

if __name__ == "__main__":
    app.run(debug=True)
