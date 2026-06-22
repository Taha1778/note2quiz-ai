import re


def clean_text(text):
    text = text.replace("\x00", " ")
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def is_text_readable(text, min_characters=50):
    if len(text.strip()) < min_characters:
        return False

    letters = sum(character.isalpha() for character in text)
    return letters >= min_characters // 2
