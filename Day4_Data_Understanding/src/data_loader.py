import json

from models import Candidate, Job


def load_candidates(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    candidates = []

    for item in data:
        candidate = Candidate(
            candidate_id=item["candidate_id"],
            name=item["name"],
            email=item["email"],
            phone=item["phone"],
            location=item["location"]
        )

        candidates.append(candidate)

    return candidates


def load_jobs(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    jobs = []

    for item in data:
        job = Job(
            job_id=item["job_id"],
            job_title=item["job_title"],
            company_name=item["company_name"],
            location=item["location"],
            job_type=item["job_type"],
            description=item["description"],
            required_skills=item.get("required_skills", []),
            preferred_skills=item.get("preferred_skills", []),
            experience_required=item.get("experience_required", ""),
            education_required=item.get("education_required", "")
        )

        jobs.append(job)

    return jobs