import re

from pypdf import PdfReader


SKILLS = [
    "python", "java", "javascript", "html", "css",
    "sql", "mysql", "mongodb", "react", "node.js",
    "machine learning", "deep learning", "artificial intelligence",
    "data analysis", "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "fastapi", "django",
    "flask", "power bi", "excel", "git", "github",
    "communication", "problem solving", "teamwork",
    "leadership", "project management", "nlp",
    "computer vision", "streamlit", "rest api"
]


def extract_resume_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text.lower()


def find_skills(text, skill_list):
    found = []

    for skill in skill_list:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return found
