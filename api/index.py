import html
import sys
from pathlib import Path

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import HTMLResponse

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from resume_analyzer import SKILLS, extract_resume_text, find_skills


app = FastAPI()


PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Resume Keyword Analyzer</title>
  <style>
    :root { color-scheme: dark; }
    body { margin: 0; background: #0e1117; color: #fafafa; font-family: Arial, sans-serif; }
    main { max-width: 760px; margin: 40px auto; padding: 24px; }
    h1 { font-size: 2rem; }
    label { display: block; margin: 18px 0 8px; font-weight: bold; }
    input, textarea, button { box-sizing: border-box; width: 100%; border-radius: 8px; }
    input, textarea { background: #262730; color: #fff; border: 1px solid #444; padding: 12px; }
    textarea { min-height: 180px; resize: vertical; }
    button { margin-top: 18px; background: #ff4b4b; color: white; border: 0; padding: 13px; font-weight: bold; cursor: pointer; }
    .card { background: #262730; border-radius: 10px; padding: 18px; margin-top: 18px; }
    .error { background: #5c1d1d; }
    .warning { background: #594d16; }
  </style>
</head>
<body>
  <main>
    <h1>📄 AI Resume Keyword Analyzer</h1>
    <p>Analyze your resume based on a job description.</p>
    __CONTENT__
  </main>
</body>
</html>"""


FORM = """
<form action="/" method="post" enctype="multipart/form-data">
  <label for="resume">Upload your resume (PDF)</label>
  <input id="resume" name="resume" type="file" accept=".pdf,application/pdf" required>
  <label for="job_description">Paste the Job Description</label>
  <textarea id="job_description" name="job_description" required></textarea>
  <button type="submit">Analyze Resume</button>
</form>
"""


@app.get("/", response_class=HTMLResponse)
async def home():
    return PAGE.replace("__CONTENT__", FORM)


@app.post("/", response_class=HTMLResponse)
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
):
    if not resume.filename.lower().endswith(".pdf"):
        content = '<div class="card error">Please upload a PDF resume.</div>' + FORM
        return PAGE.replace("__CONTENT__", content)

    if not job_description.strip():
        content = '<div class="card error">Please enter a job description.</div>' + FORM
        return PAGE.replace("__CONTENT__", content)

    try:
        resume_text = extract_resume_text(resume.file)
        jd_text = job_description.lower()
        resume_skills = find_skills(resume_text, SKILLS)
        required_skills = find_skills(jd_text, SKILLS)
        matched_skills = [skill for skill in required_skills if skill in resume_skills]
        missing_skills = [skill for skill in required_skills if skill not in resume_skills]

        if not required_skills:
            content = (
                '<div class="card warning">No supported skills were found '
                'in the job description.</div>' + FORM
            )
        else:
            score = len(matched_skills) / len(required_skills) * 100
            content = f"""
            {FORM}
            <div class="card">
              <h2>Analysis Results</h2>
              <h3>Resume Match Score: {score:.2f}%</h3>
              <progress value="{score:.0f}" max="100" style="width:100%"></progress>
              <p><strong>Matched Skills:</strong> {len(matched_skills)}</p>
              <p><strong>Skills Found:</strong> {html.escape(', '.join(matched_skills)) if matched_skills else 'No matching skills found.'}</p>
              <p><strong>Missing Skills:</strong> {html.escape(', '.join(missing_skills)) if missing_skills else 'No missing skills!'}</p>
              <p><strong>Resume Skills:</strong> {html.escape(', '.join(resume_skills)) if resume_skills else 'No supported skills found.'}</p>
              <p><em>Suggestion: Consider adding relevant missing skills only if you genuinely have those skills.</em></p>
            </div>
            """
    except Exception as exc:
        content = f'<div class="card error">Unable to analyze PDF: {html.escape(str(exc))}</div>' + FORM

    return PAGE.replace("__CONTENT__", content)
