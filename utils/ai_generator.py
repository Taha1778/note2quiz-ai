from huggingface_hub import InferenceClient


DEFAULT_MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
UNSUPPORTED_MODEL_REPLACEMENTS = {
    "Qwen/Qwen2.5-7B-Instruct-1M": DEFAULT_MODEL_ID,
}
MODEL_CHOICES = [
    "Qwen/Qwen2.5-7B-Instruct",
    "openai/gpt-oss-20b",
    "Qwen/Qwen3.5-9B",
    "meta-llama/Llama-3.1-8B-Instruct",
]
PROVIDER_CHOICES = [
    "auto",
    "together",
    "novita",
    "nscale",
    "groq",
    "fireworks-ai",
    "ovhcloud",
    "deepinfra",
]


def build_study_guide_prompt(lecture_text, difficulty, mcq_count, output_options):
    selected_outputs = "\n".join(f"- {option}" for option in output_options)

    return f"""
You are an expert AI study assistant for students.

Create a clear Markdown study guide from the lecture text.

Difficulty level: {difficulty}
Number of MCQs: {mcq_count}

The user selected these output sections:
{selected_outputs}

Rules:
- Use simple, student-friendly language.
- Keep headings clear and consistent.
- If formulas are selected but no formulas are found, write: "No clear formulas were found."
- If MCQs are selected, each MCQ must have 4 choices, the correct answer, and a short explanation.
- If flashcards are selected, use Front/Back format.
- Do not invent facts that are not supported by the lecture text.

Use this Markdown structure where relevant:

# Study Guide

## Short Summary

## Detailed Summary

## Key Points

## Key Definitions

## Important Formulas

## MCQ Questions

## Short Answer Questions

## Flashcards

## Weak Topics

## Study Plan

Lecture text:
{lecture_text}
    """.strip()


def _message_content(response):
    message = response.choices[0].message
    content = getattr(message, "content", None)

    if content:
        return content

    if isinstance(message, dict):
        return message.get("content", "")

    return str(message)


def generate_study_guide(
    lecture_text,
    api_key,
    model_id=DEFAULT_MODEL_ID,
    provider=None,
    difficulty="Medium",
    mcq_count=10,
    output_options=None,
):
    if output_options is None:
        output_options = [
            "Short summary",
            "Detailed summary",
            "Key points",
            "Definitions",
            "Formulas",
            "MCQs",
            "Short-answer questions",
            "Flashcards",
            "Study plan",
        ]

    client_kwargs = {
        "model": model_id,
        "token": api_key,
        "timeout": 120,
    }

    if provider:
        client_kwargs["provider"] = provider

    client = InferenceClient(**client_kwargs)
    prompt = build_study_guide_prompt(
        lecture_text=lecture_text,
        difficulty=difficulty,
        mcq_count=mcq_count,
        output_options=output_options,
    )

    response = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content": "You create accurate, structured study guides from lecture notes.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=3000,
        temperature=0.3,
    )

    content = _message_content(response).strip()

    if not content:
        raise RuntimeError("The model returned an empty response.")

    return content
