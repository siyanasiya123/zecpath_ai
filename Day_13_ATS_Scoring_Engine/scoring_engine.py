# Day 13 - ATS Scoring Engine

from weight_config import get_weights


def calculate_skill_match(candidate_skills, required_skills):
    """
    Calculate percentage of required skills matched by the candidate.
    """

    if not required_skills:
        return 0.0

    candidate_skills = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    required_skills = {
        skill.lower().strip()
        for skill in required_skills
    }

    matched_skills = candidate_skills.intersection(
        required_skills
    )

    score = (
        len(matched_skills) /
        len(required_skills)
    ) * 100

    return round(score, 2)


def calculate_experience_relevance(
    candidate_experience,
    required_experience
):
    """
    Calculate experience relevance based on
    candidate and required experience.
    """

    if required_experience <= 0:
        return 100.0

    score = (
        candidate_experience /
        required_experience
    ) * 100

    return round(
        min(score, 100),
        2
    )


def calculate_education_alignment(
    candidate_education,
    required_education
):
    """
    Calculate education alignment score.
    """

    if not required_education:
        return 100.0

    candidate = candidate_education.lower().strip()
    required = required_education.lower().strip()

    if candidate == required:
        return 100.0

    if required in candidate or candidate in required:
        return 80.0

    return 0.0


def calculate_semantic_similarity(
    similarity_score
):
    """
    Convert semantic similarity score into percentage.
    """

    if similarity_score is None:
        return 0.0

    return round(
        similarity_score * 100,
        2
    )


def calculate_final_score(
    skill_score,
    experience_score,
    education_score,
    semantic_score,
    role
):
    """
    Calculate the weighted ATS score.
    """

    weights = get_weights(role)

    final_score = (
        skill_score *
        weights["skill_match"]
        +
        experience_score *
        weights["experience_relevance"]
        +
        education_score *
        weights["education_alignment"]
        +
        semantic_score *
        weights["semantic_similarity"]
    )

    return round(
        final_score,
        2
    )


def get_score_category(score):
    """
    Convert ATS score into a candidate category.
    """

    if score >= 80:
        return "Strong Match"

    if score >= 65:
        return "Good Match"

    if score >= 50:
        return "Moderate Match"

    return "Low Match"


def generate_candidate_score(
    candidate,
    job
):
    """
    Generate complete ATS score for a candidate.
    """

    role = job.get(
        "role",
        "default"
    )

    skill_score = calculate_skill_match(
        candidate.get("skills", []),
        job.get("required_skills", [])
    )

    experience_score = calculate_experience_relevance(
        candidate.get("experience_years", 0),
        job.get("required_experience_years", 0)
    )

    education_score = calculate_education_alignment(
        candidate.get("education", ""),
        job.get("required_education", "")
    )

    semantic_score = calculate_semantic_similarity(
        candidate.get("semantic_similarity", 0)
    )

    final_score = calculate_final_score(
        skill_score,
        experience_score,
        education_score,
        semantic_score,
        role
    )

    return {
        "skill_match": skill_score,
        "experience_relevance": experience_score,
        "education_alignment": education_score,
        "semantic_similarity": semantic_score,
        "final_score": final_score,
        "category": get_score_category(
            final_score
        )
    }


if __name__ == "__main__":

    candidate = {
        "skills": [
            "Python",
            "FastAPI",
            "Machine Learning",
            "SQL",
            "Git"
        ],

        "experience_years": 2,

        "education": "MCA",

        "semantic_similarity": 0.86
    }

    job = {
        "role": "AI Engineer",

        "required_skills": [
            "Python",
            "FastAPI",
            "Machine Learning",
            "SQL",
            "Docker"
        ],

        "required_experience_years": 2,

        "required_education": "MCA"
    }

    result = generate_candidate_score(
        candidate,
        job
    )

    print("\n======================================")
    print("ATS SCORING ENGINE")
    print("======================================")

    print(
        "\nSkill Match:",
        result["skill_match"],
        "%"
    )

    print(
        "Experience Relevance:",
        result["experience_relevance"],
        "%"
    )

    print(
        "Education Alignment:",
        result["education_alignment"],
        "%"
    )

    print(
        "Semantic Similarity:",
        result["semantic_similarity"],
        "%"
    )

    print(
        "\nFinal ATS Score:",
        result["final_score"],
        "/ 100"
    )

    print(
        "Candidate Category:",
        result["category"]
    )