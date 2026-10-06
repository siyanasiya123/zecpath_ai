# Day 13 - Explainable ATS Output


def generate_explanation(score_result):
    """
    Generate a human-readable explanation
    for the candidate's ATS score.
    """

    explanations = []

    skill_score = score_result.get("skill_match", 0)
    experience_score = score_result.get("experience_relevance", 0)
    education_score = score_result.get("education_alignment", 0)
    semantic_score = score_result.get("semantic_similarity", 0)

    # Skill explanation
    if skill_score >= 80:
        explanations.append(
            "Strong match with the required skills."
        )
    elif skill_score >= 50:
        explanations.append(
            "The candidate matches some of the required skills."
        )
    else:
        explanations.append(
            "Several required skills are missing."
        )

    # Experience explanation
    if experience_score >= 80:
        explanations.append(
            "The candidate has highly relevant experience."
        )
    elif experience_score >= 50:
        explanations.append(
            "The candidate has partially relevant experience."
        )
    else:
        explanations.append(
            "The candidate has limited relevant experience."
        )

    # Education explanation
    if education_score >= 80:
        explanations.append(
            "The candidate's education aligns well with the role."
        )
    elif education_score >= 50:
        explanations.append(
            "The candidate's education has partial alignment."
        )
    else:
        explanations.append(
            "The candidate's education does not strongly align with the role."
        )

    # Semantic explanation
    if semantic_score >= 80:
        explanations.append(
            "Resume content has high semantic similarity with the job description."
        )
    elif semantic_score >= 60:
        explanations.append(
            "Resume content has moderate semantic similarity with the job description."
        )
    else:
        explanations.append(
            "Resume content has low semantic similarity with the job description."
        )

    return explanations


def create_explainable_output(
    score_result,
    role
):
    """
    Create a transparent and explainable
    candidate scoring result.
    """

    explanations = generate_explanation(
        score_result
    )

    return {
        "target_role": role,
        "score_breakdown": {
            "skill_match": score_result.get(
                "skill_match",
                0
            ),
            "experience_relevance": score_result.get(
                "experience_relevance",
                0
            ),
            "education_alignment": score_result.get(
                "education_alignment",
                0
            ),
            "semantic_similarity": score_result.get(
                "semantic_similarity",
                0
            )
        },
        "final_score": score_result.get(
            "final_score",
            0
        ),
        "category": score_result.get(
            "category",
            "Unknown"
        ),
        "explanation": explanations
    }


if __name__ == "__main__":

    sample_result = {
        "skill_match": 80.0,
        "experience_relevance": 100.0,
        "education_alignment": 100.0,
        "semantic_similarity": 86.0,
        "final_score": 88.2,
        "category": "Strong Match"
    }

    result = create_explainable_output(
        sample_result,
        "AI Engineer"
    )

    print("\n======================================")
    print("EXPLAINABLE ATS SCORE")
    print("======================================")

    print(
        "\nTarget Role:",
        result["target_role"]
    )

    print(
        "Final Score:",
        result["final_score"],
        "/ 100"
    )

    print(
        "Category:",
        result["category"]
    )

    print("\nScore Breakdown:")

    for parameter, score in result[
        "score_breakdown"
    ].items():

        print(
            f"{parameter}: {score}%"
        )

    print("\nExplanation:")

    for explanation in result[
        "explanation"
    ]:

        print(
            "-",
            explanation
        )
        