import re


# Resume section names and their common heading variations
SECTION_HEADINGS = {
    "Skills": [
        "skills",
        "technical skills",
        "core skills",
        "key skills",
        "technical competencies",
        "areas of expertise",
    ],
    "Work Experience": [
        "work experience",
        "professional experience",
        "employment history",
        "work history",
        "career history",
        "experience",
    ],
    "Education": [
        "education",
        "academic background",
        "educational qualifications",
        "academic qualifications",
    ],
    "Certifications": [
        "certifications",
        "certificates",
        "professional certifications",
        "licenses and certifications",
    ],
    "Projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects",
        "project experience",
    ],
}


def normalize_heading(text):
    """Normalize a possible resume heading."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s&]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def detect_section_heading(line):
    """Identify whether a line matches a known resume section heading."""
    normalized = normalize_heading(line)

    for section, headings in SECTION_HEADINGS.items():
        for heading in headings:
            if normalized == normalize_heading(heading):
                return section

    return None


def classify_resume(text):
    """
    Split resume text into sections based on recognized headings.

    Returns a dictionary containing section names and their text.
    """
    sections = {
        section: [] for section in SECTION_HEADINGS
    }

    sections["Other"] = []

    current_section = "Other"

    lines = text.splitlines()

    for line in lines:
        cleaned_line = line.strip()

        if not cleaned_line:
            continue

        detected_section = detect_section_heading(cleaned_line)

        if detected_section:
            current_section = detected_section
            continue

        sections[current_section].append(cleaned_line)

    # Convert collected lines into readable strings
    return {
        section: "\n".join(content).strip()
        for section, content in sections.items()
    }


def classify_resume_blocks(text):
    """
    Return labeled text blocks for structured JSON output.
    """
    result = classify_resume(text)

    labeled_blocks = []

    for section, content in result.items():
        if content:
            labeled_blocks.append({
                "section": section,
                "text": content
            })

    return labeled_blocks


if __name__ == "__main__":
    sample_resume = """
    SOFTWARE DEVELOPER

    Skills
    Python, Flask, SQL, Machine Learning

    Work Experience
    Python Developer Intern at ABC Company
    Developed web applications using Flask.

    Education
    MCA - Computer Applications

    Certifications
    Python Programming Certificate

    Projects
    AI Resume Analyzer
    Developed a resume analysis application.
    """

    output = classify_resume(sample_resume)

    for section, content in output.items():
        if content:
            print(f"\n--- {section} ---")
            print(content)