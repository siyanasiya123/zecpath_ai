# -------------------------------------------------
# Education Relevance Scorer
# -------------------------------------------------

ROLE_EDUCATION_KEYWORDS = {

    "AI Engineer": [
        "computer science",
        "computer applications",
        "artificial intelligence",
        "machine learning",
        "data science",
        "information technology",
        "software engineering",
        "technology",
        "engineering"
    ],

    "Machine Learning Engineer": [
        "computer science",
        "computer applications",
        "artificial intelligence",
        "machine learning",
        "data science",
        "information technology",
        "software engineering",
        "engineering"
    ],

    "Data Scientist": [
        "data science",
        "computer science",
        "computer applications",
        "statistics",
        "mathematics",
        "artificial intelligence",
        "machine learning"
    ],

    "Data Analyst": [
        "data analytics",
        "data analysis",
        "statistics",
        "mathematics",
        "computer science",
        "computer applications",
        "business analytics",
        "business administration"
    ],

    "Python Developer": [
        "computer science",
        "computer applications",
        "information technology",
        "software engineering",
        "technology",
        "engineering"
    ],

    "Software Engineer": [
        "computer science",
        "computer applications",
        "information technology",
        "software engineering",
        "technology",
        "engineering"
    ]
}


# -------------------------------------------------
# Normalize Text
# -------------------------------------------------

def normalize_text(text):
    """
    Normalize text for comparison.
    """

    if not text:
        return ""

    return (
        text
        .lower()
        .strip()
        .replace("-", " ")
        .replace("_", " ")
    )


# -------------------------------------------------
# Calculate Education Relevance
# -------------------------------------------------

def calculate_education_relevance(
    education,
    target_role
):
    """
    Calculate education relevance for a target role.

    Returns a score between 0 and 100.
    """

    if not education:
        return 0

    target_role = target_role.strip()

    keywords = ROLE_EDUCATION_KEYWORDS.get(
        target_role,
        []
    )

    if not keywords:
        return 0

    total_score = 0
    education_count = 0

    for qualification in education:

        degree = normalize_text(
            qualification.get(
                "degree",
                ""
            )
        )

        field = normalize_text(
            qualification.get(
                "field_of_study",
                ""
            )
        )

        combined_text = (
            degree + " " + field
        )

        score = 0

        # Strong match through field of study
        for keyword in keywords:

            normalized_keyword = normalize_text(
                keyword
            )

            if normalized_keyword in field:
                score = 100
                break

        # Degree-based match
        if score == 0:

            for keyword in keywords:

                normalized_keyword = normalize_text(
                    keyword
                )

                if normalized_keyword in combined_text:
                    score = 80
                    break

        total_score += score
        education_count += 1

    if education_count == 0:
        return 0

    return round(
        total_score / education_count,
        2
    )


# -------------------------------------------------
# Relevance Category
# -------------------------------------------------

def get_relevance_category(score):
    """
    Convert numerical score into a readable category.
    """

    if score >= 80:
        return "Highly Relevant"

    if score >= 50:
        return "Relevant"

    if score >= 25:
        return "Partially Relevant"

    return "Low Relevance"


# -------------------------------------------------
# Main Test
# -------------------------------------------------

if __name__ == "__main__":

    sample_education = [
        {
            "degree": "Master of Computer Applications",
            "field_of_study": "Computer Applications",
            "institution": "University of Calicut",
            "graduation_year": 2026
        }
    ]

    target_role = "AI Engineer"

    score = calculate_education_relevance(
        sample_education,
        target_role
    )

    category = get_relevance_category(
        score
    )

    print("Target Role:", target_role)
    print("Education Relevance Score:", score)
    print("Relevance Category:", category)