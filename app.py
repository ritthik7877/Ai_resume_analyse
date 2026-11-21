
import streamlit as st
import re
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Keyword Analyzer")
st.write("Analyze your resume based on a job description.")

# Extract text from uploaded PDF
def extract_resume_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text.lower()


# Available skills and keywords
skills = [
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


# Find matching skills
def find_skills(text, skill_list):
    found = []

    for skill in skill_list:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return found


# Resume upload
uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

# Job description input
job_description = st.text_area(
    "Paste the Job Description",
    height=200
)


if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload your resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:
        try:
            resume_text = extract_resume_text(uploaded_file)
            jd_text = job_description.lower()

            resume_skills = find_skills(
                resume_text, skills
            )

            required_skills = find_skills(
                jd_text, skills
            )

            matched_skills = [
                skill for skill in required_skills
                if skill in resume_skills
            ]

            missing_skills = [
                skill for skill in required_skills
                if skill not in resume_skills
            ]

            if not required_skills:
                st.warning(
                    "No supported skills were found "
                    "in the job description."
                )
            else:
                score = (
                    len(matched_skills)
                    / len(required_skills)
                ) * 100

                st.subheader("Analysis Results")

                st.metric(
                    "Resume Match Score",
                    f"{score:.2f}%"
                )

                st.progress(int(score))

                st.success(
                    f"Matched Skills: {len(matched_skills)}"
                )

                st.write("### ✅ Skills Found")
                if matched_skills:
                    st.write(", ".join(matched_skills))
                else:
                    st.write("No matching skills found.")

                st.write("### ❌ Missing Skills")
                if missing_skills:
                    st.write(", ".join(missing_skills))
                else:
                    st.write("No missing skills!")

                st.write("### 📋 Resume Skills")
                st.write(", ".join(resume_skills))

                st.info(
                    "Suggestion: Consider adding relevant "
                    "missing skills only if you genuinely "
                    "have those skills."
                )

        except Exception as e:
            st.error(f"Unable to analyze PDF: {e}")
