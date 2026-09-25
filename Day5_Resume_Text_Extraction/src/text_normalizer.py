import re


SECTION_HEADINGS = {
    "education": "EDUCATION",
    "educational qualification": "EDUCATION",
    "experience": "EXPERIENCE",
    "work experience": "EXPERIENCE",
    "skills": "SKILLS",
    "technical skills": "SKILLS",
    "projects": "PROJECTS",
    "project": "PROJECTS",
    "certifications": "CERTIFICATIONS",
    "certification": "CERTIFICATIONS",
    "summary": "SUMMARY",
    "profile": "SUMMARY",
    "objective": "SUMMARY",
}


def normalize_bullets(text):
    text = text.replace("•", "-")
    text = text.replace("▪", "-")
    text = text.replace("●", "-")
    text = text.replace("◦", "-")

    return text


def normalize_headings(text):

    lines = []

    for line in text.splitlines():

        stripped = line.strip()

        key = stripped.lower().rstrip(":")

        if key in SECTION_HEADINGS:
            lines.append(SECTION_HEADINGS[key])
        else:
            lines.append(stripped)

    return "\n".join(lines)


def normalize_text(text):

    text = normalize_bullets(text)

    text = normalize_headings(text)

    # Remove unnecessary spaces before punctuation
    text = re.sub(r"\s+([,.;:])", r"\1", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()