
# 📄 AI Resume Keyword Analyzer

An intelligent web-based application built using Python that analyzes resumes against job descriptions. It identifies matching skills, missing keywords, and calculates a resume match percentage to help candidates improve their resumes.

## 🚀 Project Overview

The AI Resume Keyword Analyzer allows users to upload their resumes in PDF format and enter a job description. The application extracts text from the resume, identifies relevant skills, compares them with the job requirements, and displays an analysis report.

## ✨ Features

- 📂 Upload resumes in PDF format.
- 📝 Enter job descriptions.
- 🔍 Extract text from uploaded resumes.
- ✅ Identify skills and matching keywords.
- ❌ Detect missing skills and keywords.
- 📊 Calculate resume match percentage.
- 💡 Provide suggestions for resume improvement.
- 🌐 Simple and user-friendly web interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| PyPDF | Extract text from PDF files |
| Regular Expressions (Regex) | Keyword identification and matching |

## 📁 Project Structure

```text
AI-Resume-Keyword-Analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd AI-Resume-Keyword-Analyzer
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 📊 How It Works

1. Upload your resume in PDF format.
2. Paste the job description into the text area.
3. Click the Analyze Resume button.
4. The application extracts text from the resume.
5. It identifies relevant skills in both the resume and job description.
6. It compares the keywords and calculates the match percentage.
7. It displays matching skills, missing skills, and improvement suggestions.

## 📈 Sample Output

- Resume Match Score: 75%
- Matched Skills: Python, SQL, HTML, CSS
- Missing Skills: Machine Learning, JavaScript
- Suggestions: Improve your resume by including relevant skills you genuinely possess.

*Note: The above is an illustrative example.*

## 🔮 Future Enhancements

- Add DOCX resume support.
- Implement NLP-based semantic matching.
- Integrate machine learning for advanced resume analysis.
- Generate personalized resume improvement suggestions.
- Add job role recommendations.
- Provide downloadable analysis reports.

## 🎯 Project Objective

The main objective of this project is to help job seekers understand how well their resumes match specific job descriptions and identify relevant skills they may need to highlight.

## 👨‍💻 Author

**Ritthik RB**

MCA Student | Aspiring AI/ML Engineer

---

⭐ If you find this project useful, consider giving the repository a star!
