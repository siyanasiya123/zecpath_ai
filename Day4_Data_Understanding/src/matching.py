from models import CandidateMatching


def calculate_skill_match(candidate_skills, required_skills):
    if not required_skills:
        return 0.0

    candidate_skill_names = {
        skill.skill_name.lower()
        for skill in candidate_skills
    }

    required_skill_names = {
        skill.lower()
        for skill in required_skills
    }

    matched_skills = candidate_skill_names.intersection(required_skill_names)

    score = (len(matched_skills) / len(required_skill_names)) * 100

    return round(score, 2)


def calculate_education_match(candidate_education, required_education):
    if not candidate_education or not required_education:
        return 0.0

    for education in candidate_education:
        if education.degree.lower() == required_education.lower():
            return 100.0

    return 0.0


def calculate_experience_match(experience_required):
    if experience_required.lower() == "fresher":
        return 100.0

    return 0.0


def create_candidate_matching(
    candidate_id,
    job_id,
    skill_match_score,
    education_match_score,
    experience_match_score
):
    overall_match_score = (
        skill_match_score * 0.5
        + education_match_score * 0.2
        + experience_match_score * 0.3
    )

    status = "Matched" if overall_match_score >= 70 else "Not Matched"

    return CandidateMatching(
        matching_id=f"M_{candidate_id}_{job_id}",
        candidate_id=candidate_id,
        job_id=job_id,
        skill_match_score=skill_match_score,
        education_match_score=education_match_score,
        experience_match_score=experience_match_score,
        overall_match_score=round(overall_match_score, 2),
        matching_status=status
    )


def get_skill_details(candidate_skills, required_skills):
    candidate_skill_names = {
        skill.skill_name.lower()
        for skill in candidate_skills
    }

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in candidate_skill_names:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills