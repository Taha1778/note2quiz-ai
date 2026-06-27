# Note2Quiz AI

Note2Quiz AI is a Streamlit app that turns lecture notes into a study guide using a Hugging Face-hosted language model.

## Features

- Upload PDF or TXT lecture files
- Extract and preview lecture text
- Clean and validate extracted text
- Generate summaries, key points, definitions, formulas, MCQs, short-answer questions, flashcards, and a study plan
- Choose difficulty and number of MCQs
- Download the generated study guide as Markdown

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- Hugging Face Hub InferenceClient

## Project Structure

```text
app.py
requirements.txt
README.md
.gitignore
utils/
  __init__.py
  file_reader.py
  text_cleaner.py
  ai_generator.py
  output_formatter.py
sample_files/
outputs/
```

## Run Locally

1. Create and activate a virtual environment.

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Run the app.

```bash
streamlit run app.py
```

4. Add your Hugging Face token in the sidebar when the app opens.

## Hugging Face Settings

The app uses this default model:

```text
Qwen/Qwen2.5-7B-Instruct
```

For deployment, add these Streamlit secrets:

```toml
HF_TOKEN = "your_hugging_face_token"
HF_MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
HF_PROVIDER = "auto"
```

If this model/provider pair does not work on your Hugging Face account, try one of the model choices shown in the app sidebar:

```text
Qwen/Qwen2.5-7B-Instruct
openai/gpt-oss-20b
Qwen/Qwen3.5-9B
meta-llama/Llama-3.1-8B-Instruct
```

Use `HF_PROVIDER = "auto"` first. If it still fails, choose a provider enabled on your Hugging Face account, such as `together`, `novita`, `nscale`, `groq`, `fireworks-ai`, `hf-inference`, or `sambanova`.

## Testing Checklist

- Upload a normal PDF
- Upload a TXT file
- Try an empty file
- Try a scanned PDF
- Test without a Hugging Face token
- Test Easy, Medium, and Exam Level difficulty
- Test 5, 10, 15, and 20 MCQs
- Download the generated Markdown guide

## Future Improvements

- Interactive quiz mode
- Score calculation
- DOCX and PPTX support
- OCR for scanned PDFs
- Saved study guides
- Chat with uploaded notes
