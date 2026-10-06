# Day 13 - Configurable ATS Weight System


ROLE_WEIGHTS = {
    "AI Engineer": {
        "skill_match": 0.40,
        "experience_relevance": 0.25,
        "education_alignment": 0.15,
        "semantic_similarity": 0.20
    },

    "Python Developer": {
        "skill_match": 0.40,
        "experience_relevance": 0.30,
        "education_alignment": 0.10,
        "semantic_similarity": 0.20
    },

    "Data Analyst": {
        "skill_match": 0.35,
        "experience_relevance": 0.25,
        "education_alignment": 0.20,
        "semantic_similarity": 0.20
    },

    "Java Backend Developer": {
        "skill_match": 0.40,
        "experience_relevance": 0.30,
        "education_alignment": 0.10,
        "semantic_similarity": 0.20
    },

    "default": {
        "skill_match": 0.40,
        "experience_relevance": 0.25,
        "education_alignment": 0.15,
        "semantic_similarity": 0.20
    }
}


def get_weights(role):
    """
    Return scoring weights based on the target job role.
    Uses default weights when the role is not configured.
    """

    return ROLE_WEIGHTS.get(
        role,
        ROLE_WEIGHTS["default"]
    )


def validate_weights(weights):
    """
    Check whether the configured weights add up to 100%.
    """

    total = sum(weights.values())

    return round(total, 2) == 1.0


if __name__ == "__main__":

    role = "AI Engineer"

    weights = get_weights(role)

    print("ATS Weight Configuration")
    print("------------------------")
    print("Role:", role)

    for parameter, weight in weights.items():
        print(
            f"{parameter}: {weight * 100:.0f}%"
        )

    print(
        "\nWeights Valid:",
        validate_weights(weights)
    )