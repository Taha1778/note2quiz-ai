import streamlit as st

from utils.ai_generator import (
    DEFAULT_MODEL_ID,
    MODEL_CHOICES,
    PROVIDER_CHOICES,
    UNSUPPORTED_MODEL_REPLACEMENTS,
    build_study_guide_prompt,
    format_generation_error,
    generate_study_guide,
)
from utils.file_reader import extract_text_from_upload
from utils.output_formatter import extract_tab_content
from utils.text_cleaner import clean_text, is_text_readable


MAX_INPUT_CHARS = 24000


st.set_page_config(
    page_title="Note2Quiz AI",
    page_icon="N2Q",
    layout="wide",
)


def get_secret(name, default=""):
    try:
        return st.secrets.get(name, default)
    except Exception:
        return default


def show_learning_steps():
    with st.sidebar.expander("Learning steps"):
        st.markdown(
            """
1. Project setup
2. Basic Streamlit page
3. Read PDF and TXT files
4. Clean and validate text
5. Connect to Hugging Face
6. Build the study-guide prompt
7. Add user controls
8. Display results clearly
9. Add Markdown download
10. Test edge cases
11. Prepare for deployment
            """.strip()
        )


st.title("Note2Quiz AI")
st.subheader("AI Study Notes Summarizer and Quiz Generator")
st.write(
    "Upload lecture notes, extract the content, and generate summaries, quizzes, "
    "flashcards, formulas, and a revision plan."
)
st.warning("Do not upload confidential, private, or sensitive files.")

show_learning_steps()

st.sidebar.header("Settings")

hf_token = get_secret("HF_TOKEN")
if not hf_token:
    hf_token = st.sidebar.text_input("Hugging Face token", type="password")

configured_model_id = get_secret("HF_MODEL_ID", DEFAULT_MODEL_ID)
if configured_model_id in UNSUPPORTED_MODEL_REPLACEMENTS:
    st.sidebar.warning(
        f"{configured_model_id} is not supported by Hugging Face Inference Providers. "
        f"Using {UNSUPPORTED_MODEL_REPLACEMENTS[configured_model_id]} instead."
    )
    configured_model_id = UNSUPPORTED_MODEL_REPLACEMENTS[configured_model_id]

model_options = list(dict.fromkeys([configured_model_id, *MODEL_CHOICES]))
model_id = st.sidebar.selectbox(
    "Hugging Face model",
    model_options,
    index=0,
    help="Choose a model that appears in the Hugging Face Inference Providers catalog.",
)

configured_provider = get_secret("HF_PROVIDER", "auto") or "auto"
provider_options = list(dict.fromkeys([configured_provider, *PROVIDER_CHOICES]))
hf_provider = st.sidebar.selectbox(
    "Hugging Face provider",
    provider_options,
    index=0,
    help="Use auto first. If it fails, try together for Qwen or another provider enabled on your account.",
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Exam Level"],
    index=1,
)

mcq_count = st.sidebar.selectbox(
    "Number of MCQs",
    [5, 10, 15, 20],
    index=1,
)

output_options = st.sidebar.multiselect(
    "Outputs to generate",
    [
        "Short summary",
        "Detailed summary",
        "Key points",
        "Definitions",
        "Formulas",
        "MCQs",
        "Short-answer questions",
        "Flashcards",
        "Study plan",
    ],
    default=[
        "Short summary",
        "Detailed summary",
        "Key points",
        "Definitions",
        "Formulas",
        "MCQs",
        "Short-answer questions",
        "Flashcards",
        "Study plan",
    ],
)

uploaded_file = st.file_uploader(
    "Upload your lecture file",
    type=["pdf", "txt"],
)

if uploaded_file is None:
    st.info("Upload a PDF or TXT lecture file to start.")
    st.stop()

try:
    raw_text = extract_text_from_upload(uploaded_file)
except ValueError as error:
    st.error(str(error))
    st.stop()
except Exception as error:
    st.error(f"Could not read this file: {error}")
    st.stop()

cleaned_text = clean_text(raw_text)

if not is_text_readable(cleaned_text):
    st.error("No readable text was found. This may be an empty file or a scanned PDF.")
    st.stop()

if len(cleaned_text) > MAX_INPUT_CHARS:
    st.warning(
        "This file is long, so only the first part will be sent to the model "
        "for this first version."
    )
    model_text = cleaned_text[:MAX_INPUT_CHARS]
else:
    model_text = cleaned_text

with st.expander("Preview extracted text", expanded=True):
    st.caption(f"Showing the first 2,000 characters from {len(cleaned_text):,} characters.")
    st.text_area(
        "Extracted text preview",
        value=cleaned_text[:2000],
        height=220,
        disabled=True,
        label_visibility="collapsed",
    )

with st.expander("Preview AI prompt"):
    st.markdown(
        build_study_guide_prompt(
            lecture_text="[lecture text will be inserted here]",
            difficulty=difficulty,
            mcq_count=mcq_count,
            output_options=output_options,
        )
    )

if not output_options:
    st.error("Choose at least one output type from the sidebar.")
    st.stop()

if st.button("Generate Study Guide", type="primary"):
    if not hf_token:
        st.error("Add your Hugging Face token in the sidebar or Streamlit secrets.")
        st.stop()

    with st.spinner("Generating your study guide with Hugging Face..."):
        try:
            study_guide = generate_study_guide(
                lecture_text=model_text,
                api_key=hf_token,
                model_id=model_id,
                provider=hf_provider,
                difficulty=difficulty,
                mcq_count=mcq_count,
                output_options=output_options,
            )
        except Exception as error:
            st.error(format_generation_error(error))
            st.stop()

    st.success("Study guide generated successfully.")

    tabs = st.tabs(["Full Guide", "Summary", "Key Points", "Quiz", "Flashcards", "Study Plan"])

    with tabs[0]:
        st.markdown(study_guide)

    with tabs[1]:
        st.markdown(
            extract_tab_content(
                study_guide,
                ["Short Summary", "Detailed Summary", "Summary"],
            )
        )

    with tabs[2]:
        st.markdown(extract_tab_content(study_guide, ["Key Points", "Key Definitions", "Important Formulas"]))

    with tabs[3]:
        st.markdown(extract_tab_content(study_guide, ["MCQ Questions", "MCQs", "Short Answer Questions"]))

    with tabs[4]:
        st.markdown(extract_tab_content(study_guide, ["Flashcards"]))

    with tabs[5]:
        st.markdown(extract_tab_content(study_guide, ["Study Plan", "Revision Plan", "Weak Topics"]))

    st.download_button(
        label="Download Study Guide",
        data=study_guide,
        file_name="generated_study_guide.md",
        mime="text/markdown",
    )
