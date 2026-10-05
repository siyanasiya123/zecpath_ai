import json
from pathlib import Path

from section_classifier import classify_resume_blocks


# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Input and output paths
INPUT_FILE = BASE_DIR / "data" / "sample_resumes.txt"
OUTPUT_FILE = BASE_DIR / "output" / "labeled_resume_samples.json"


def main():
    # Check whether the input file exists
    if not INPUT_FILE.exists():
        print(f"Error: Resume file not found: {INPUT_FILE}")
        return

    # Read resume text
    resume_text = INPUT_FILE.read_text(encoding="utf-8")

    # Classify resume sections
    labeled_blocks = classify_resume_blocks(resume_text)

    # Prepare structured JSON output
    result = {
        "resume_file": INPUT_FILE.name,
        "total_sections_detected": len(labeled_blocks),
        "sections": labeled_blocks
    }

    # Create output folder if needed
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Save JSON output
    OUTPUT_FILE.write_text(
        json.dumps(result, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    print("Resume section classification completed successfully!")
    print(f"Output saved to: {OUTPUT_FILE}")
    print("\nClassified Sections:")
    print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()