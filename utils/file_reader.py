from pathlib import Path

import fitz


def extract_text_from_pdf(uploaded_file):
    pdf_bytes = uploaded_file.getvalue()
    text_parts = []

    with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
        for page in document:
            text_parts.append(page.get_text())

    return "\n".join(text_parts)


def extract_text_from_txt(uploaded_file):
    file_bytes = uploaded_file.getvalue()

    try:
        return file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return file_bytes.decode("latin-1")


def extract_text_from_upload(uploaded_file):
    suffix = Path(uploaded_file.name).suffix.lower()

    if suffix == ".pdf":
        return extract_text_from_pdf(uploaded_file)

    if suffix == ".txt":
        return extract_text_from_txt(uploaded_file)

    raise ValueError("Unsupported file type. Please upload a PDF or TXT file.")
