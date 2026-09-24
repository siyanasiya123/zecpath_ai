import json
import os
import re


INPUT_FILE = "extracted_data/raw_resume_data.json"
OUTPUT_FILE = "extracted_data/resume_data.json"


def find_section(text, section_name, next_sections):
    """
    Extract content between one section heading
    and the next section heading.
    """

    pattern = rf"{section_name}\s*(.*?)(?=\n(?:{'|'.join(next_sections)})\s*|\Z)"

    match = re.search(
        pattern,
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return ""


def extract_name(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines:
        return lines[0]

    return ""


def extract_email(text):
    match = re.search(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        text
    )

    return match.group(0) if match else ""


def extract_phone(text):
    match = re.search(
        r"\+91[\s-]?\d{5}[\s-]?\d{5}",
        text
    )

    return match.group(0) if match else ""


def extract_designation(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if len(lines) >= 2:
        return lines[1]

    return ""


def create_structured_resume(resume):

    text = resume["raw_text"]

    skills = find_section(
        text,
        "SKILLS",
        [
            "EXPERIENCE",
            "EDUCATION",
            "CERTIFICATIONS",
            "PROJECTS"
        ]
    )

    experience = find_section(
        text,
        "EXPERIENCE",
        [
            "EDUCATION",
            "CERTIFICATIONS",
            "PROJECTS"
        ]
    )

    education = find_section(
        text,
        "EDUCATION",
        [
            "CERTIFICATIONS",
            "PROJECTS"
        ]
    )

    certifications = find_section(
        text,
        "CERTIFICATIONS",
        [
            "PROJECTS"
        ]
    )

    projects = find_section(
        text,
        "PROJECTS",
        []
    )

    structured_data = {
        "resume_file": resume["resume_file"],

        "candidate_profile": {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
            "designation": extract_designation(text)
        },

        "skills": [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ],

        "experience": experience,

        "education": education,

        "certifications": [
            certifications
        ] if certifications else [],

        "projects": [
            projects
        ] if projects else []
    }

    return structured_data


def main():

    if not os.path.exists(INPUT_FILE):

        print("ERROR: raw_resume_data.json not found.")

        print(
            "Run extract_resume.py first."
        )

        return

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        resumes = json.load(file)

    structured_resumes = []

    for resume in resumes:

        print(
            f"Structuring: {resume['resume_file']}"
        )

        structured_resume = create_structured_resume(
            resume
        )

        structured_resumes.append(
            structured_resume
        )

    os.makedirs(
        "extracted_data",
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            structured_resumes,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\n" + "=" * 60)
    print("RESUME STRUCTURING COMPLETED")
    print("=" * 60)

    print(
        f"Total resumes structured: {len(structured_resumes)}"
    )

    print(
        f"Output: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()