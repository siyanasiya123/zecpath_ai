import json
from pathlib import Path

from education_parser import parse_education
from certification_parser import parse_certifications
from relevance_scorer import (
    calculate_education_relevance,
    get_relevance_category
)


BASE_DIR = Path(__file__).resolve().parent

RESUME_FILE = BASE_DIR / "data" / "sample_resumes.txt"
JOB_FILE = BASE_DIR / "data" / "job_requirements.txt"
OUTPUT_FILE = BASE_DIR / "output" / "structured_academic_profile.json"


def read_file(file_path):
    """Read text from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_target_role(job_text):
    """Extract target job role from job requirements."""
    for line in job_text.splitlines():
        if line.upper().startswith("JOB ROLE:"):
            return line.split(":", 1)[1].strip()

    return "Unknown"


def split_resumes(resume_text):
    """Split the sample file into individual resumes."""
    sections = resume_text.split("RESUME ")

    resumes = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        lines = section.splitlines()

        resume_number = lines[0].strip()
        content = "\n".join(lines[1:]).strip()

        resumes.append(
            {
                "resume_id": f"RESUME {resume_number}",
                "text": content
            }
        )

    return resumes


def process_resumes():
    """Process all resumes and create structured academic profiles."""

    resume_text = read_file(RESUME_FILE)
    job_text = read_file(JOB_FILE)

    target_role = extract_target_role(job_text)

    resumes = split_resumes(resume_text)

    structured_profiles = []

    for resume in resumes:

        education = parse_education(resume["text"])

        certifications = parse_certifications(resume["text"])

        relevance_score = calculate_education_relevance(
            education,
            target_role
        )

        relevance_category = get_relevance_category(
            relevance_score
        )

        profile = {
            "resume_id": resume["resume_id"],
            "target_role": target_role,
            "education": education,
            "certifications": certifications,
            "education_relevance": {
                "score": relevance_score,
                "category": relevance_category
            }
        }

        structured_profiles.append(profile)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            structured_profiles,
            file,
            indent=4
        )

    print("\n======================================")
    print("DAY 11 PROCESSING COMPLETED")
    print("======================================")

    print("Target Role:", target_role)
    print("Resumes Processed:", len(structured_profiles))

    for profile in structured_profiles:

        print("\n", profile["resume_id"])

        print(
            "Education:",
            len(profile["education"])
        )

        print(
            "Certifications:",
            len(profile["certifications"])
        )

        print(
            "Education Relevance:",
            profile["education_relevance"]["score"],
            "%",
            "-",
            profile["education_relevance"]["category"]
        )

    print("\nOutput saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    process_resumes()