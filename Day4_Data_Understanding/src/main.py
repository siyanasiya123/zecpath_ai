from models import (
    Candidate,
    Skill,
    Education,
    Project,
    Job,
    JobApplication,
    CandidateMatching
)

from relationships import (
    CandidateProfile,
    JobProfile,
    ApplicationDetails
)

from data_loader import load_candidates, load_jobs

from matching import (
    calculate_skill_match,
    calculate_education_match,
    calculate_experience_match,
    create_candidate_matching,
    get_skill_details
)


# =========================
# SAMPLE OBJECTS
# =========================

candidate = Candidate(
    candidate_id="C001",
    name="Siyana Sherin",
    email="siyana@example.com",
    phone="9876543210",
    location="Kerala"
)


skill = Skill(
    skill_id="S001",
    skill_name="Python",
    category="Programming",
    level="Intermediate"
)


education = Education(
    education_id="E001",
    degree="MCA",
    specialization="Computer Applications",
    institution="KTU",
    graduation_year=2027,
    cgpa_or_percentage="8.1"
)


project = Project(
    project_id="P001",
    project_name="AI Resume Analyzer",
    description="An AI-based system for analyzing resumes.",
    technologies=["Python", "Streamlit", "Gemini"],
    role="Developer"
)


job = Job(
    job_id="J001",
    job_title="AI/ML Intern",
    company_name="ABC Technologies",
    location="Kochi",
    job_type="Internship",
    description="AI and Machine Learning internship",
    required_skills=["Python", "Machine Learning"],
    preferred_skills=["Django", "Deep Learning"],
    experience_required="Fresher",
    education_required="MCA"
)


application = JobApplication(
    application_id="A001",
    candidate_id="C001",
    job_id="J001",
    application_date="2026-09-24",
    status="Applied",
    match_score=85.5
)


matching = CandidateMatching(
    matching_id="M001",
    candidate_id="C001",
    job_id="J001",
    skill_match_score=90.0,
    education_match_score=95.0,
    experience_match_score=80.0,
    overall_match_score=88.5,
    matching_status="Matched"
)


# =========================
# DISPLAY OBJECTS
# =========================

print("===== CANDIDATE =====")
print(candidate)

print("\n===== SKILL =====")
print(skill)

print("\n===== EDUCATION =====")
print(education)

print("\n===== PROJECT =====")
print(project)

print("\n===== JOB =====")
print(job)

print("\n===== JOB APPLICATION =====")
print(application)

print("\n===== CANDIDATE MATCHING =====")
print(matching)


# =========================
# CREATE PROFILES
# =========================

candidate_profile = CandidateProfile(
    candidate=candidate,
    skills=[skill],
    education=[education],
    projects=[project]
)

job_profile = JobProfile(
    job=job,
    applications=[application]
)

application_details = ApplicationDetails(
    application=application,
    matching=matching
)


# =========================
# DISPLAY RELATIONSHIPS
# =========================

print("\n===== CANDIDATE PROFILE =====")
print(candidate_profile)

print("\n===== JOB PROFILE =====")
print(job_profile)

print("\n===== APPLICATION DETAILS =====")
print(application_details)


# =========================
# LOAD CANDIDATES FROM JSON
# =========================

print("\n===== LOADED CANDIDATES FROM JSON =====")

candidates = load_candidates("data/candidates.json")

for candidate_item in candidates:
    print(candidate_item)


# =========================
# LOAD JOBS FROM JSON
# =========================

print("\n===== LOADED JOBS FROM JSON =====")

jobs = load_jobs("data/jobs.json")

for job_item in jobs:
    print(job_item)


# =========================
# CANDIDATE-JOB MATCHING
# =========================

candidate_skills = [skill]

candidate_education = [education]

print("\n===== CANDIDATE-JOB MATCHING =====")

skill_score = calculate_skill_match(
    candidate_skills,
    job.required_skills
)

education_score = calculate_education_match(
    candidate_education,
    job.education_required
)

experience_score = calculate_experience_match(
    job.experience_required
)

matching_result = create_candidate_matching(
    candidate_id=candidate.candidate_id,
    job_id=job.job_id,
    skill_match_score=skill_score,
    education_match_score=education_score,
    experience_match_score=experience_score
)

print("Candidate:", candidate.name)
print("Job:", job.job_title)
print("Skill Match:", skill_score, "%")
print("Education Match:", education_score, "%")
print("Experience Match:", experience_score, "%")
print("Overall Match:", matching_result.overall_match_score, "%")
print("Status:", matching_result.matching_status)


# =========================
# MATCH CANDIDATE WITH ALL JOBS
# =========================

print("\n===== ALL JOB MATCHING RESULTS =====")

for job_item in jobs:

    skill_score = calculate_skill_match(
        candidate_skills,
        job_item.required_skills
    )

    education_score = calculate_education_match(
        candidate_education,
        job_item.education_required
    )

    experience_score = calculate_experience_match(
        job_item.experience_required
    )

    result = create_candidate_matching(
        candidate_id=candidate.candidate_id,
        job_id=job_item.job_id,
        skill_match_score=skill_score,
        education_match_score=education_score,
        experience_match_score=experience_score
    )

    matched_skills, missing_skills = get_skill_details(
        candidate_skills,
        job_item.required_skills
    )

    print("\nJob:", job_item.job_title)
    print("Company:", job_item.company_name)
    print("Matched Skills:", matched_skills)
    print("Missing Skills:", missing_skills)
    print("Skill Match:", skill_score, "%")
    print("Education Match:", education_score, "%")
    print("Experience Match:", experience_score, "%")
    print("Overall Match:", result.overall_match_score, "%")
    print("Status:", result.matching_status)