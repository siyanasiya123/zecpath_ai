import re


def clean_encoding(text):
    """Fix common UTF-8 encoding issues."""

    if not text:
        return ""

    replacements = {
        "â€“": "-",
        "â€”": "-",
        "â€˜": "'",
        "â€™": "'",
        "â€œ": '"',
        "â€": '"',
        "â€¢": "*",
        "Â": ""
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    if match:
        return match.group(0)

    return ""


def extract_phone(text):
    match = re.search(r'\+91[\s-]?\d{5}[\s-]?\d{5}', text)

    if match:
        return match.group(0)

    return ""


def extract_name(text):
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if lines:
        return lines[0]

    return ""


def extract_location(text):
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    for line in lines:
        if "|" in line:
            parts = [part.strip() for part in line.split("|")]

            for part in parts:
                if "," in part and "@" not in part and "+91" not in part:
                    return part

    return ""


def get_section(text, start_heading, end_headings):
    """Extract text between section headings."""

    lines = text.splitlines()

    collected = []
    inside_section = False

    headings = {
        heading.upper()
        for heading in end_headings
    }

    for line in lines:
        stripped = line.strip()

        if stripped.upper() == start_heading.upper():
            inside_section = True
            continue

        if inside_section and stripped.upper() in headings:
            break

        if inside_section and stripped:
            collected.append(stripped)

    return collected


def extract_skills(text):
    skills_lines = get_section(
        text,
        "SKILLS",
        [
            "EXPERIENCE",
            "EDUCATION",
            "CERTIFICATIONS",
            "PROJECTS"
        ]
    )

    if not skills_lines:
        return []

    skills_text = " ".join(skills_lines)

    skills = [
        skill.strip()
        for skill in skills_text.split(",")
        if skill.strip()
    ]

    return skills


def extract_summary(text):
    summary_lines = get_section(
        text,
        "PROFESSIONAL SUMMARY",
        [
            "SKILLS",
            "EXPERIENCE",
            "EDUCATION",
            "CERTIFICATIONS",
            "PROJECTS"
        ]
    )

    return " ".join(summary_lines).strip()


def extract_experience(text):
    return get_section(
        text,
        "EXPERIENCE",
        [
            "EDUCATION",
            "CERTIFICATIONS",
            "PROJECTS"
        ]
    )


def extract_education(text):
    return get_section(
        text,
        "EDUCATION",
        [
            "CERTIFICATIONS",
            "PROJECTS"
        ]
    )


def extract_certifications(text):
    return get_section(
        text,
        "CERTIFICATIONS",
        [
            "PROJECTS"
        ]
    )


def extract_projects(text):
    return get_section(
        text,
        "PROJECTS",
        []
    )


def extract_resume_data(text):
    """Extract structured information from resume text."""

    text = clean_encoding(text)

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "location": extract_location(text),
        "skills": extract_skills(text),
        "summary": extract_summary(text),
        "experience": extract_experience(text),
        "education": extract_education(text),
        "certifications": extract_certifications(text),
        "projects": extract_projects(text)
    }