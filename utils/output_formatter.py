import re


def _normalize_heading(heading):
    return re.sub(r"[^a-z0-9]+", " ", heading.lower()).strip()


def extract_markdown_sections(markdown_text):
    pattern = re.compile(r"^(#{2,3})\s+(.+?)\s*$", re.MULTILINE)
    matches = list(pattern.finditer(markdown_text))
    sections = {}

    for index, match in enumerate(matches):
        heading = match.group(2).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown_text)
        sections[_normalize_heading(heading)] = markdown_text[start:end].strip()

    return sections


def extract_tab_content(markdown_text, headings):
    sections = extract_markdown_sections(markdown_text)
    content_parts = []

    for heading in headings:
        normalized = _normalize_heading(heading)
        for section_heading, body in sections.items():
            if normalized in section_heading or section_heading in normalized:
                content_parts.append(f"## {heading}\n\n{body}")
                break

    if content_parts:
        return "\n\n".join(content_parts)

    return "This section was not found in the generated output. Check the Full Guide tab."
