import json
import os

from experience_parser import (
    parse_experience,
    calculate_total_experience,
    detect_gaps,
    detect_overlaps
)

from relevance_scorer import calculate_relevance


# -----------------------------
# File Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RESUME_FILE = os.path.join(
    BASE_DIR,
    "data",
    "sample_resumes.txt"
)

JOB_FILE = os.path.join(
    BASE_DIR,
    "data",
    "job_requirements.txt"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "structured_experience_output.json"
)


# -----------------------------
# Read Job Requirements
# -----------------------------

def read_job_requirements():
    """Read target role from the job requirements file."""

    with open(JOB_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    target_role = "Unknown Role"

    for line in content.splitlines():
        if line.upper().startswith("JOB ROLE:"):
            target_role = line.split(":", 1)[1].strip()
            break

    return target_role


# -----------------------------
# Read Resume Samples
# -----------------------------

def read_resume_samples():
    """Read and separate multiple resume samples."""

    with open(RESUME_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    resumes = []

    sections = content.split("RESUME ")

    for section in sections:
        section = section.strip()

        if not section:
            continue

        lines = section.splitlines()

        resume_id = lines[0].strip()

        resume_text = "\n".join(lines[1:]).strip()

        resumes.append({
            "resume_id": f"RESUME {resume_id}",
            "text": resume_text
        })

    return resumes


# -----------------------------
# Process Resumes
# -----------------------------

def process_resumes():
    """Parse experience and calculate relevance for all resumes."""

    target_role = read_job_requirements()
    resumes = read_resume_samples()

    results = []

    for resume in resumes:

        # Extract professional experience
        experiences = parse_experience(resume["text"])

        # Calculate total experience
        total_months = calculate_total_experience(experiences)

        # Detect employment gaps
        gaps = detect_gaps(experiences)

        # Detect overlapping employment
        overlaps = detect_overlaps(experiences)

        # Calculate relevance score for each role
        for experience in experiences:

            job_title = experience.get(
                "job_title",
                ""
            )

            relevance_score = calculate_relevance(
                job_title,
                target_role
            )

            experience["relevance_score"] = relevance_score

        # Create structured result
        structured_resume = {
            "resume_id": resume["resume_id"],
            "target_role": target_role,
            "total_experience_months": total_months,
            "total_experience_years": round(
                total_months / 12,
                2
            ),
            "gaps": gaps,
            "overlaps": overlaps,
            "experiences": experiences
        }

        results.append(structured_resume)

    return results


# -----------------------------
# Save Output
# -----------------------------

def save_output(results):
    """Save structured experience data as JSON."""

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4,
            ensure_ascii=False
        )


# -----------------------------
# Main Program
# -----------------------------

def main():

    print("=" * 60)
    print("DAY 10 - EXPERIENCE PARSING & RELEVANCE ENGINE")
    print("=" * 60)

    print("\nReading resume samples...")

    results = process_resumes()

    save_output(results)

    print("\nProcessing completed successfully.")

    print(f"\nTotal resumes processed: {len(results)}")

    print(f"\nOutput file created:")
    print(OUTPUT_FILE)

    print("\n" + "=" * 60)

    # Display summary
    for result in results:

        print(f"\n{result['resume_id']}")
        print(f"Target Role: {result['target_role']}")
        print(
            f"Total Experience: "
            f"{result['total_experience_months']} months "
            f"({result['total_experience_years']} years)"
        )

        print(
            f"Gaps Detected: "
            f"{len(result['gaps'])}"
        )

        print(
            f"Overlaps Detected: "
            f"{len(result['overlaps'])}"
        )

        print("Roles:")

        for experience in result["experiences"]:

            print(
                f"  - {experience['job_title']} "
                f"at {experience['company']} "
                f"| Relevance: "
                f"{experience['relevance_score']}%"
            )

    print("\n" + "=" * 60)
    print("Structured output saved successfully.")
    print("=" * 60)


# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":
    main()