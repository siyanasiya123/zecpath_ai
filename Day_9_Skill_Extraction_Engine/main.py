import json
from pathlib import Path

from skill_extractor import extract_skills


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "data" / "sample_resumes.txt"
OUTPUT_FILE = BASE_DIR / "output" / "structured_skill_output.json"


def split_resumes(text):
    """Split the sample file into individual resumes."""

    parts = text.split("RESUME ")

    resumes = []

    for part in parts:
        if part.strip():
            lines = part.strip().splitlines()

            resume_id = lines[0].strip()

            resume_text = "\n".join(lines[1:]).strip()

            resumes.append({
                "resume_id": resume_id,
                "text": resume_text
            })

    return resumes


def main():

    if not INPUT_FILE.exists():
        print("Sample resume file not found.")
        return

    text = INPUT_FILE.read_text(encoding="utf-8")

    resumes = split_resumes(text)

    results = []

    for resume in resumes:

        skills = extract_skills(resume["text"])

        results.append({
            "resume_id": resume["resume_id"],
            "total_skills": len(skills),
            "skills": skills
        })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        json.dumps(results, indent=4),
        encoding="utf-8"
    )

    print("Skill extraction completed successfully.")
    print(f"Processed resumes: {len(results)}")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()