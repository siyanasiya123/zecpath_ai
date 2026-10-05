import re


ROLE_KEYWORDS = {
    "ai engineer": [
        "ai",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "python",
        "generative ai",
        "llm",
        "rag"
    ],
    "machine learning engineer": [
        "machine learning",
        "deep learning",
        "python",
        "tensorflow",
        "pytorch",
        "nlp"
    ],
    "python developer": [
        "python",
        "flask",
        "fastapi",
        "django",
        "rest api",
        "sql"
    ],
    "data analyst": [
        "python",
        "pandas",
        "sql",
        "data analysis",
        "power bi",
        "excel"
    ]
}


def normalize(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def calculate_role_similarity(job_title, target_role):
    """
    Calculate role-to-role similarity based on keyword overlap.
    """

    job_title = normalize(job_title)
    target_role = normalize(target_role)

    if job_title == target_role:
        return 1.0

    target_keywords = set(
        ROLE_KEYWORDS.get(target_role, target_role.split())
    )

    title_words = set(job_title.split())

    if not target_keywords:
        return 0.0

    overlap = len(title_words.intersection(target_keywords))

    return round(
        min(overlap / len(target_keywords), 1.0),
        2
    )


def calculate_relevance(job_title, target_role):
    """
    Calculate experience relevance score.

    Returns a score between 0 and 100.
    """

    similarity = calculate_role_similarity(
        job_title,
        target_role
    )

    return round(similarity * 100, 2)