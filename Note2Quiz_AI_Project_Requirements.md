# Note2Quiz AI — Study Notes Summarizer and Quiz Generator

## 1. Project Overview

**Project name:** Note2Quiz AI  
**Project type:** AI/NLP web application  
**Difficulty:** Beginner to intermediate  
**Deployment difficulty:** Easy  
**Recommended deployment:** Streamlit Community Cloud  
**Main goal:** Allow students to upload lecture notes, extract the content, summarize it, and generate quiz questions, flashcards, and revision material.

This project is designed to be simple enough to build and deploy, but strong enough to put on your GitHub, CV, LinkedIn, or scholarship application portfolio.

---

## 2. Problem Statement

Students often have long lecture notes, PDFs, slides, and revision files. Before exams, they need to quickly understand the important concepts, formulas, definitions, and possible questions.

The problem is that manually summarizing notes and creating quizzes takes a lot of time.

This app solves that by using AI to convert uploaded study material into:

- Simple summaries
- Detailed summaries
- Key points
- Important definitions
- Important formulas
- MCQ questions
- Short-answer questions
- Flashcards
- Weak-topic revision suggestions

---

## 3. Target Users

The main users are:

1. University students
2. Engineering students
3. Medical students
4. High school students
5. People studying for certificates or online courses

For your first version, you can focus on:

> Engineering students who upload lecture PDFs and want a summary, formulas, and exam-style questions.

---

## 4. Main Features

## 4.1 Must-Have Features — Version 1

These are the features you should build first.

### 1. Upload lecture file

The user should be able to upload a file.

Supported file types in version 1:

- `.pdf`
- `.txt`

Optional later:

- `.docx`
- `.pptx`

### 2. Extract text from file

The app should extract readable text from the uploaded file.

For PDFs, use:

```python
PyMuPDF
```

For TXT files, use normal Python file reading.

### 3. Display extracted text preview

After uploading, show the first part of the extracted text.

Example:

```text
Preview:
OFDM stands for Orthogonal Frequency Division Multiplexing...
```

This helps the user confirm that the file was read correctly.

### 4. Generate short summary

The user should be able to generate a short version of the lecture.

Example output:

```text
This lecture explains the basics of OFDM, including subcarriers, orthogonality, cyclic prefix, and how OFDM reduces multipath interference.
```

### 5. Generate detailed summary

The app should generate a more structured summary with headings.

Example:

```markdown
## OFDM Overview
OFDM divides high-speed data into multiple lower-speed streams.

## Orthogonality
Subcarriers are mathematically arranged so they do not interfere with each other.

## Cyclic Prefix
A cyclic prefix is added to reduce inter-symbol interference.
```

### 6. Extract key points

The app should give bullet points of the most important ideas.

Example:

```text
- OFDM uses multiple subcarriers.
- Subcarriers are orthogonal.
- Cyclic prefix reduces ISI.
- OFDM is used in Wi-Fi, LTE, and 5G.
```

### 7. Extract important definitions

The app should identify definitions from the lecture.

Example:

```text
Orthogonality:
A condition where subcarriers do not interfere with each other.

Cyclic Prefix:
A repeated part of the OFDM symbol added at the beginning to reduce interference.
```

### 8. Extract important formulas

The app should try to find formulas or equations.

Example:

```text
Subcarrier spacing:
Δf = 1 / T

Symbol duration:
T_total = T_symbol + T_cp
```

If no formulas are found, the app should say:

```text
No clear formulas were detected in this file.
```

### 9. Generate MCQ questions

The app should create multiple-choice questions.

Each question should include:

- Question text
- 4 answer choices
- Correct answer
- Explanation

Example:

```text
1. What is the main purpose of the cyclic prefix in OFDM?

A. Increase the carrier frequency
B. Reduce inter-symbol interference
C. Remove modulation
D. Decrease bandwidth

Correct answer: B

Explanation:
The cyclic prefix helps reduce inter-symbol interference caused by multipath propagation.
```

### 10. Generate short-answer questions

The app should generate short-answer revision questions.

Example:

```text
1. Explain why OFDM is useful in multipath channels.
2. What is the difference between FDM and OFDM?
3. Why are subcarriers in OFDM called orthogonal?
```

### 11. Generate flashcards

Flashcards should have a front and back.

Example:

```text
Front:
What does OFDM stand for?

Back:
Orthogonal Frequency Division Multiplexing.
```

### 12. Download generated study guide

The user should be able to download the generated output as a `.txt` or `.md` file.

Version 1 recommended:

- `.txt` download

Version 2 upgrade:

- `.pdf` download
- `.docx` download

---

## 5. Nice-to-Have Features — Version 2

After version 1 works, add these.

### 1. Difficulty selector

The user can choose:

- Easy
- Medium
- Exam level

Example:

```text
Choose difficulty:
[Easy] [Medium] [Exam Level]
```

The AI output should change based on the selected difficulty.

### 2. Number of questions selector

The user can choose how many questions they want.

Example:

```text
Number of MCQs: 5, 10, 15, 20
```

### 3. Quiz mode

Instead of only showing questions and answers, the app can let the user answer inside the website.

Example:

```text
Question 1:
What is OFDM?

A. ...
B. ...
C. ...
D. ...

Submit Answer
```

Then show:

```text
Correct!
```

or

```text
Wrong. The correct answer is B.
```

### 4. Score calculation

At the end of the quiz, show the score.

Example:

```text
Your score: 7/10
```

### 5. Weak-topic detection

Based on wrong answers, the app tells the user what to revise.

Example:

```text
Weak topics:
- Cyclic prefix
- Subcarrier spacing
- Orthogonality
```

### 6. Study plan generator

The app creates a short revision plan.

Example:

```text
Today:
- Revise OFDM basics
- Memorize definitions
- Solve 5 MCQs

Tomorrow:
- Practice numerical questions
- Review cyclic prefix
```

### 7. Support DOCX files

Use:

```python
python-docx
```

### 8. Support PowerPoint files

Use:

```python
python-pptx
```

### 9. OCR for scanned PDFs

If the PDF is scanned images and not selectable text, use OCR.

Possible tools:

```python
pytesseract
easyocr
```

This is optional and can be added later because it makes deployment more complicated.

---

## 6. Recommended Tech Stack

## 6.1 Basic Stack

Use this for your first version.

```text
Frontend/web app: Streamlit
PDF extraction: PyMuPDF
AI model/API: Gemini API or OpenAI API
Language: Python
Deployment: Streamlit Community Cloud
Version control: GitHub
```

## 6.2 Why This Stack?

### Streamlit

Streamlit lets you create a website using only Python.

You will use it for:

- File upload
- Buttons
- Dropdowns
- Tabs
- Displaying summaries
- Displaying quiz questions
- Download button

### PyMuPDF

PyMuPDF reads PDF files and extracts text.

You will use it for:

- Opening PDF
- Reading each page
- Extracting text from the lecture

### Gemini API or OpenAI API

The AI API generates:

- Summaries
- MCQs
- Flashcards
- Definitions
- Study plans

### GitHub

GitHub stores your code online.

You will use it to:

- Save your project
- Track changes
- Connect to Streamlit Cloud for deployment

### Streamlit Community Cloud

This hosts your app online and gives you a public link.

Example final link:

```text
https://note2quiz-ai.streamlit.app
```

---

## 7. Project Folder Structure

Create your project folder like this:

```text
note2quiz-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── __init__.py
│   ├── pdf_reader.py
│   ├── text_cleaner.py
│   ├── ai_generator.py
│   └── output_formatter.py
│
├── sample_files/
│   └── sample_lecture.pdf
│
└── outputs/
    └── generated_study_guide.md
```

### Explanation of each file

## `app.py`

This is the main Streamlit app.

It controls:

- Page title
- File upload
- Buttons
- User selections
- Displaying results

## `requirements.txt`

This file contains the Python libraries needed for deployment.

Example:

```text
streamlit
pymupdf
python-dotenv
google-generativeai
```

Or if using OpenAI:

```text
streamlit
pymupdf
python-dotenv
openai
```

## `README.md`

This explains your project on GitHub.

It should include:

- Project description
- Features
- Tech stack
- How to run locally
- Screenshots
- Deployment link

## `.gitignore`

This prevents sensitive or unnecessary files from being uploaded to GitHub.

Example:

```text
.env
__pycache__/
outputs/
```

## `utils/pdf_reader.py`

Contains code for extracting text from PDFs.

## `utils/text_cleaner.py`

Contains code for cleaning extracted text.

## `utils/ai_generator.py`

Contains code for sending prompts to the AI model.

## `utils/output_formatter.py`

Contains code for formatting the final study guide.

## `sample_files/`

Contains sample PDFs to test your app.

## `outputs/`

Contains generated study guides locally.

---

## 8. Functional Requirements

Functional requirements describe what the system must do.

## FR1 — File Upload

The system shall allow the user to upload a `.pdf` or `.txt` file.

## FR2 — File Type Validation

The system shall check that the uploaded file type is supported.

Supported in version 1:

```text
.pdf
.txt
```

If unsupported, show:

```text
Unsupported file type. Please upload a PDF or TXT file.
```

## FR3 — Text Extraction

The system shall extract text from the uploaded file.

For PDF:

- Open file using PyMuPDF
- Loop over all pages
- Extract text page by page

For TXT:

- Read the file directly

## FR4 — Empty Text Handling

If no text is extracted, show:

```text
No readable text was found. This may be a scanned PDF.
```

## FR5 — Text Preview

The system shall display a preview of the extracted text.

Example:

```text
Showing first 1000 characters...
```

## FR6 — Output Selection

The system shall allow the user to choose which outputs to generate.

Options:

- Short summary
- Detailed summary
- Key points
- Definitions
- Formulas
- MCQs
- Short-answer questions
- Flashcards
- Study plan

## FR7 — Difficulty Selection

The system shall allow the user to choose difficulty.

Options:

```text
Easy
Medium
Exam Level
```

## FR8 — MCQ Count Selection

The system shall allow the user to choose the number of MCQs.

Options:

```text
5
10
15
20
```

## FR9 — AI Generation

The system shall send the extracted text and selected options to the AI model.

## FR10 — Display Output

The system shall display the generated study guide clearly on the page.

## FR11 — Download Output

The system shall allow the user to download the generated result.

Recommended version 1 format:

```text
Markdown file
```

## FR12 — Error Handling

The system shall handle:

- No file uploaded
- Unsupported file type
- Empty extracted text
- AI API error
- Very long files
- Internet/API connection issues

---

## 9. Non-Functional Requirements

Non-functional requirements describe the quality of the system.

## NFR1 — Usability

The app should be simple and clear for students.

The user should understand what to do without instructions.

## NFR2 — Performance

For normal lecture files, output should be generated within a reasonable time.

Target:

```text
Small file: under 20 seconds
Medium file: under 60 seconds
```

## NFR3 — Security

The API key must not be uploaded to GitHub.

Use:

```text
.env file locally
Streamlit secrets in deployment
```

## NFR4 — Privacy

The app should tell users not to upload private or sensitive documents.

Add a warning:

```text
Do not upload confidential, private, or sensitive files.
```

## NFR5 — Maintainability

The code should be organized into separate files.

Do not put everything inside `app.py`.

## NFR6 — Scalability

The first version can handle one file at a time.

Later, you can add multiple file upload.

## NFR7 — Reliability

The app should not crash if:

- The file is empty
- The PDF has no text
- The API fails
- The file is too large

---

## 10. UI Requirements

## 10.1 Page Layout

Use this layout:

```text
Title
Project description
File uploader
Output options
Difficulty selector
Question count selector
Generate button
Results section
Download button
```

## 10.2 Suggested Tabs

Use Streamlit tabs:

```text
Tab 1: Summary
Tab 2: Key Points
Tab 3: Quiz
Tab 4: Flashcards
Tab 5: Study Plan
```

## 10.3 Suggested Sidebar

Use the sidebar for settings:

```text
Sidebar:
- Difficulty
- Number of MCQs
- Output type
- About project
```

## 10.4 Color and Style

Keep it clean.

Suggested style:

```text
White background
Blue or purple accent
Simple headings
Clear boxes
No complicated design
```

---

## 11. Exact Development Steps

## Step 1 — Create project folder

Create a folder on your computer:

```bash
mkdir note2quiz-ai
cd note2quiz-ai
```

---

## Step 2 — Create virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Create required files

Create:

```bash
app.py
requirements.txt
README.md
.gitignore
```

Create folders:

```bash
mkdir utils
mkdir sample_files
mkdir outputs
```

Inside `utils`, create:

```bash
pdf_reader.py
text_cleaner.py
ai_generator.py
output_formatter.py
__init__.py
```

---

## Step 4 — Install libraries

If using Gemini API:

```bash
pip install streamlit pymupdf python-dotenv google-generativeai
```

If using OpenAI API:

```bash
pip install streamlit pymupdf python-dotenv openai
```

---

## Step 5 — Create requirements.txt

If using Gemini API:

```text
streamlit
pymupdf
python-dotenv
google-generativeai
```

If using OpenAI API:

```text
streamlit
pymupdf
python-dotenv
openai
```

---

## Step 6 — Build PDF reader

Create `utils/pdf_reader.py`.

```python
import fitz


def extract_text_from_pdf(uploaded_file):
    text = ""

    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page in doc:
        text += page.get_text()
        text += "\n"

    return text
```

---

## Step 7 — Build TXT reader

You can put this in `app.py` or a separate utility file.

```python
def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")
```

---

## Step 8 — Build text cleaner

Create `utils/text_cleaner.py`.

```python
def clean_text(text):
    text = text.replace("\x00", " ")
    text = text.replace("\n\n", "\n")
    text = " ".join(text.split())
    return text
```

---

## Step 9 — Build AI generator

Create `utils/ai_generator.py`.

### Option A — Gemini version

```python
import os
import google.generativeai as genai


def configure_gemini(api_key):
    genai.configure(api_key=api_key)


def generate_study_guide(text, difficulty="Medium", mcq_count=10):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f'''
You are an AI study assistant.

Create a study guide from the following lecture text.

Difficulty level: {difficulty}
Number of MCQs: {mcq_count}

Your output must include:
1. Short summary
2. Detailed summary
3. Key points
4. Key definitions
5. Important formulas if available
6. {mcq_count} MCQs with answers and explanations
7. 5 short-answer questions
8. 10 flashcards
9. Suggested revision plan

Lecture text:
{text}
'''

    response = model.generate_content(prompt)
    return response.text
```

### Option B — OpenAI version

```python
from openai import OpenAI


def generate_study_guide(text, api_key, difficulty="Medium", mcq_count=10):
    client = OpenAI(api_key=api_key)

    prompt = f'''
You are an AI study assistant.

Create a study guide from the following lecture text.

Difficulty level: {difficulty}
Number of MCQs: {mcq_count}

Your output must include:
1. Short summary
2. Detailed summary
3. Key points
4. Key definitions
5. Important formulas if available
6. {mcq_count} MCQs with answers and explanations
7. 5 short-answer questions
8. 10 flashcards
9. Suggested revision plan

Lecture text:
{text}
'''

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You create clear study guides for students."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
```

---

## Step 10 — Build the Streamlit app

Create `app.py`.

Gemini version:

```python
import streamlit as st
import os
from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.ai_generator import configure_gemini, generate_study_guide


st.set_page_config(
    page_title="Note2Quiz AI",
    page_icon="📘",
    layout="wide"
)

st.title("📘 Note2Quiz AI")
st.subheader("AI Study Notes Summarizer and Quiz Generator")

st.write(
    "Upload lecture notes and generate summaries, MCQs, flashcards, and a revision plan."
)

st.warning("Do not upload private, confidential, or sensitive files.")

api_key = st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    api_key = st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    configure_gemini(api_key)

uploaded_file = st.file_uploader(
    "Upload your lecture file",
    type=["pdf", "txt"]
)

difficulty = st.selectbox(
    "Choose difficulty",
    ["Easy", "Medium", "Exam Level"]
)

mcq_count = st.selectbox(
    "Number of MCQs",
    [5, 10, 15, 20]
)

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        raw_text = extract_text_from_pdf(uploaded_file)
    elif file_type == "txt":
        raw_text = uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file type.")
        st.stop()

    cleaned_text = clean_text(raw_text)

    if len(cleaned_text) < 50:
        st.error("No readable text was found. This may be a scanned PDF.")
        st.stop()

    with st.expander("Preview extracted text"):
        st.write(cleaned_text[:2000])

    if st.button("Generate Study Guide"):
        with st.spinner("Generating your study guide..."):
            try:
                study_guide = generate_study_guide(
                    cleaned_text,
                    difficulty=difficulty,
                    mcq_count=mcq_count
                )

                st.success("Study guide generated successfully!")

                st.markdown(study_guide)

                st.download_button(
                    label="Download Study Guide",
                    data=study_guide,
                    file_name="generated_study_guide.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
```

---

## Step 11 — Add `.gitignore`

Create `.gitignore`.

```text
.env
__pycache__/
outputs/
venv/
.streamlit/secrets.toml
```

---

## Step 12 — Test locally

Run:

```bash
streamlit run app.py
```

Open the local link in your browser.

Usually:

```text
http://localhost:8501
```

Test with:

- Small PDF
- TXT file
- Empty file
- PDF with very little text
- Long lecture file

---

## Step 13 — Create GitHub repository

Go to GitHub and create a new repository:

```text
note2quiz-ai
```

Then upload your project.

Commands:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_LINK
git push -u origin main
```

Replace:

```text
YOUR_GITHUB_REPO_LINK
```

with your actual GitHub repo link.

---

## Step 14 — Deploy on Streamlit Community Cloud

1. Go to Streamlit Community Cloud.
2. Sign in using GitHub.
3. Click **New app**.
4. Select your repository.
5. Choose branch:

```text
main
```

6. Main file path:

```text
app.py
```

7. Add your API key in secrets.

For Gemini:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

8. Click deploy.

After deployment, you will get a public app link.

---

## 12. Recommended AI Prompt

Use this prompt inside your project.

```text
You are an expert AI study assistant.

Your task is to convert lecture notes into a complete study guide.

The student may be preparing for an engineering or university exam.

Use clear, simple language.

Create the following sections:

1. Short Summary
Write a 5-line summary of the lecture.

2. Detailed Summary
Break the lecture into clear headings and explain each topic.

3. Key Points
List the most important ideas as bullet points.

4. Key Definitions
Extract and explain important terms.

5. Important Formulas
List formulas, equations, rules, and when to use them.
If no formulas exist, write: "No clear formulas were found."

6. MCQ Questions
Create MCQ questions with 4 choices each.
Mark the correct answer.
Explain why the answer is correct.

7. Short Answer Questions
Create short-answer questions that test understanding.

8. Flashcards
Create flashcards in Front/Back format.

9. Weak Topics to Revise
Suggest the topics the student should revise most.

10. 2-Day Revision Plan
Create a simple 2-day study plan.

Difficulty level: {difficulty}
Number of MCQs: {mcq_count}

Lecture text:
{text}
```

---

## 13. Example Output Format

The AI should output something like this:

```markdown
# Study Guide

## 1. Short Summary

This lecture explains...

## 2. Detailed Summary

### Topic 1: ...

Explanation...

### Topic 2: ...

Explanation...

## 3. Key Points

- Point 1
- Point 2
- Point 3

## 4. Key Definitions

**Term:** Explanation

## 5. Important Formulas

Formula:
Explanation:

## 6. MCQs

### Question 1
Question text?

A. Option 1  
B. Option 2  
C. Option 3  
D. Option 4  

**Correct answer:** B

**Explanation:** ...

## 7. Short Answer Questions

1. Question...
2. Question...

## 8. Flashcards

**Front:** Question  
**Back:** Answer

## 9. Weak Topics to Revise

- Topic 1
- Topic 2

## 10. 2-Day Revision Plan

### Day 1
- ...

### Day 2
- ...
```

---

## 14. Testing Checklist

Before deployment, test these cases.

## File upload tests

- [ ] Upload a normal PDF
- [ ] Upload a TXT file
- [ ] Upload unsupported file
- [ ] Upload empty file
- [ ] Upload scanned PDF

## AI output tests

- [ ] Summary generated correctly
- [ ] MCQs generated correctly
- [ ] Correct answers shown
- [ ] Explanations included
- [ ] Flashcards generated
- [ ] Formulas extracted if available

## UI tests

- [ ] App title appears
- [ ] File uploader works
- [ ] Difficulty selector works
- [ ] MCQ count selector works
- [ ] Generate button works
- [ ] Download button works
- [ ] Error messages are clear

## Deployment tests

- [ ] App runs locally
- [ ] requirements.txt is correct
- [ ] API key is not uploaded to GitHub
- [ ] Streamlit secrets are set
- [ ] Public app link works

---

## 15. Suggested GitHub README

Use this as your `README.md`.

```markdown
# Note2Quiz AI

Note2Quiz AI is an AI-powered study assistant that converts lecture notes into summaries, quiz questions, flashcards, and revision plans.

## Features

- Upload PDF or TXT lecture notes
- Extract text automatically
- Generate short and detailed summaries
- Extract key points and definitions
- Generate MCQ questions with answers
- Generate flashcards
- Create a revision plan
- Download the final study guide

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- Gemini API / OpenAI API
- Streamlit Community Cloud

## How to Run Locally

```bash
git clone YOUR_REPO_LINK
cd note2quiz-ai
pip install -r requirements.txt
streamlit run app.py
```

## Deployment

The app is deployed using Streamlit Community Cloud.

## Future Improvements

- Quiz mode
- Score calculation
- Weak-topic analysis
- DOCX support
- PowerPoint support
- OCR for scanned PDFs
```

---

## 16. Portfolio Description

Use this on your CV or LinkedIn.

```text
Built Note2Quiz AI, an AI-powered web app that converts lecture notes into structured study guides. The system allows users to upload PDF or TXT files, extracts the text, and generates summaries, key definitions, MCQs, flashcards, and revision plans using a large language model. The app was developed with Python, Streamlit, PyMuPDF, and an AI API, then deployed online using Streamlit Community Cloud.
```

---

## 17. Suggested LinkedIn Post

```text
I built Note2Quiz AI, an AI-powered study assistant that helps students turn lecture notes into summaries, quiz questions, flashcards, and revision plans.

The project was built using Python, Streamlit, PyMuPDF, and an AI language model API.

Main features:
- Upload PDF or TXT lecture notes
- Generate short and detailed summaries
- Extract definitions and formulas
- Create MCQs with answers and explanations
- Generate flashcards
- Download a complete study guide

This project helped me practice NLP, prompt engineering, document processing, web app development, and deployment.
```

---

## 18. Future Upgrade Roadmap

## Version 1 — Basic app

- Upload PDF/TXT
- Extract text
- Generate study guide
- Download Markdown file

## Version 2 — Better study tool

- Quiz mode
- Score calculation
- Difficulty control
- Better UI
- DOCX support

## Version 3 — Advanced AI project

- Weak-topic detection
- Student progress tracking
- Login system
- Saved study guides
- OCR for scanned PDFs
- Multiple file upload

## Version 4 — Strong portfolio version

- RAG system
- Chat with lecture notes
- Vector database
- User dashboard
- Personalized study plans

---

## 19. What You Should Do Exactly

Follow this order.

### Phase 1 — Setup

1. Install Python.
2. Install VS Code.
3. Create project folder.
4. Create virtual environment.
5. Install Streamlit and PyMuPDF.
6. Create file structure.

### Phase 2 — Basic App

1. Create Streamlit page.
2. Add file uploader.
3. Read PDF/TXT file.
4. Show extracted text preview.
5. Add Generate button.

### Phase 3 — AI Integration

1. Choose Gemini or OpenAI API.
2. Create API key.
3. Store API key safely.
4. Write AI prompt.
5. Send extracted text to AI.
6. Display generated study guide.

### Phase 4 — Download Feature

1. Format generated output as Markdown.
2. Add download button.
3. Test downloaded file.

### Phase 5 — Testing

1. Test with 3 different PDFs.
2. Test with 1 TXT file.
3. Test with a bad file.
4. Test with a scanned PDF.
5. Fix errors.

### Phase 6 — GitHub

1. Create GitHub repo.
2. Push code.
3. Write README.
4. Add screenshots.
5. Make repo public.

### Phase 7 — Deployment

1. Open Streamlit Community Cloud.
2. Connect GitHub.
3. Select repo.
4. Add API key to secrets.
5. Deploy app.
6. Copy final app link.

### Phase 8 — Portfolio

1. Add GitHub link to CV.
2. Add deployed app link to CV.
3. Post project on LinkedIn.
4. Add screenshots to your portfolio.

---

## 20. Minimum Version You Need to Finish

If you want the simplest complete version, build only this:

```text
Upload PDF
Extract text
Send text to AI
Generate summary + 10 MCQs + flashcards
Display result
Download as Markdown
Deploy on Streamlit Cloud
```

This is enough to count as a complete AI side project.

---

## 21. Final Deliverables

By the end, you should have:

```text
1. GitHub repository
2. Deployed Streamlit app link
3. README file
4. Screenshots
5. Sample lecture file
6. Downloadable generated study guide
7. Short portfolio description
```

---

## 22. Recommended Final Project Title

Use:

```text
Note2Quiz AI
```

Subtitle:

```text
AI Study Notes Summarizer and Quiz Generator
```

This title is clear, professional, and easy to understand.
