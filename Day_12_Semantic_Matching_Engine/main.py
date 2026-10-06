import json
import re
from pathlib import Path

from matching_engine import compare_resume_with_job


BASE_DIR = Path(__file__).resolve().parent

RESUME_FILE = BASE_DIR / "data" / "sample_resumes.txt"
JOB_FILE = BASE_DIR / "data" / "job_descriptions.txt"
OUTPUT_FILE = BASE_DIR / "output" / "semantic_matching_results.json"


def read_file(file_path):
    """Read text from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def parse_resume_sections(resume_text):
    """Convert resume text into structured sections."""

    sections = {
        "skills": "",
        "experience": "",
        "projects": ""
    }

    current_section = None

    for line in resume_text.splitlines():

        line = line.strip()

        if not line:
            continue

        upper_line = line.upper()

        if upper_line.startswith("SKILLS:"):
            current_section = "skills"
            sections["skills"] = line.split(":", 1)[1].strip()

        elif upper_line.startswith("EXPERIENCE:"):
            current_section = "experience"
            sections["experience"] = line.split(":", 1)[1].strip()

        elif upper_line.startswith("PROJECTS:"):
            current_section = "projects"
            sections["projects"] = line.split(":", 1)[1].strip()

        elif current_section:
            sections[current_section] += " " + line

    return sections


def parse_job_sections(job_text):
    """Convert job description into structured sections."""

    job = {
        "job_title": "",
        "skills": "",
        "experience": "",
        "projects": ""
    }

    current_section = None

    for line in job_text.splitlines():

        line = line.strip()

        if not line:
            continue

        upper_line = line.upper()

        if upper_line.startswith("JOB TITLE:"):
            job["job_title"] = line.split(":", 1)[1].strip()
            current_section = None

        elif upper_line.startswith("SKILLS:"):
            current_section = "skills"
            job["skills"] = line.split(":", 1)[1].strip()

        elif upper_line.startswith("EXPERIENCE:"):
            current_section = "experience"
            job["experience"] = line.split(":", 1)[1].strip()

        elif upper_line.startswith("PROJECTS:"):
            current_section = "projects"
            job["projects"] = line.split(":", 1)[1].strip()

        elif current_section:
            job[current_section] += " " + line

    return job


def split_resumes(text):
    """Split sample resume file into individual resumes."""

    pattern = r"RESUME\s+(\d+)"

    matches = list(re.finditer(pattern, text))

    resumes = []

    for index, match in enumerate(matches):

        resume_number = match.group(1)

        start = match.end()

        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        structured_resume = parse_resume_sections(content)

        resumes.append({
            "resume_id": f"RESUME {resume_number}",
            **structured_resume
        })

    return resumes


def split_jobs(text):
    """Split job description file using JOB number headings only."""

    pattern = r"(?m)^JOB\s+(\d+)\s*$"

    matches = list(re.finditer(pattern, text))

    jobs = []

    for index, match in enumerate(matches):

        job_number = match.group(1)

        start = match.end()

        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        structured_job = parse_job_sections(content)

        jobs.append({
            "job_id": f"JOB {job_number}",
            **structured_job
        })

    return jobs


def process_matching():

    resume_text = read_file(RESUME_FILE)
    job_text = read_file(JOB_FILE)

    resumes = split_resumes(resume_text)
    jobs = split_jobs(job_text)

    results = []

    for resume in resumes:

        for job in jobs:

            matching_result = compare_resume_with_job(
                resume,
                job
            )

            result = {
                "resume_id": resume["resume_id"],
                "job_id": job["job_id"],
                "job_title": job["job_title"],
                "matching_result": matching_result
            }

            results.append(result)

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
            results,
            file,
            indent=4
        )

    print("\n======================================")
    print("DAY 12 SEMANTIC MATCHING COMPLETED")
    print("======================================")

    print("Resumes Processed:", len(resumes))
    print("Jobs Processed:", len(jobs))
    print("Total Comparisons:", len(results))

    for result in results:

        overall = result["matching_result"]["overall"]

        print(
            f"\n{result['resume_id']} -> "
            f"{result['job_id']} "
            f"({result['job_title']})"
        )

        print(
            "Overall Similarity:",
            overall["similarity_percentage"],
            "%"
        )

        print(
            "Category:",
            overall["category"]
        )

    print("\nResults saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    process_matching()