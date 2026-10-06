from embedding_engine import generate_embedding
from similarity_scorer import (
    calculate_similarity,
    similarity_percentage,
    get_similarity_category
)


def calculate_text_similarity(resume_text, job_text):
    """
    Generate embeddings for two texts and calculate
    their semantic similarity.
    """

    resume_embedding = generate_embedding(resume_text)
    job_embedding = generate_embedding(job_text)

    score = calculate_similarity(
        resume_embedding,
        job_embedding
    )

    return {
        "similarity_score": score,
        "similarity_percentage": similarity_percentage(score),
        "category": get_similarity_category(score)
    }


def compare_resume_with_job(resume, job_description):
    """
    Compare a resume with a job description using
    semantic similarity.
    """

    skills_score = calculate_text_similarity(
        resume.get("skills", ""),
        job_description.get("skills", "")
    )

    experience_score = calculate_text_similarity(
        resume.get("experience", ""),
        job_description.get("experience", "")
    )

    projects_score = calculate_text_similarity(
        resume.get("projects", ""),
        job_description.get("projects", "")
    )

    overall_resume = " ".join([
        resume.get("skills", ""),
        resume.get("experience", ""),
        resume.get("projects", "")
    ])

    overall_job = " ".join([
        job_description.get("skills", ""),
        job_description.get("experience", ""),
        job_description.get("projects", "")
    ])

    overall_score = calculate_text_similarity(
        overall_resume,
        overall_job
    )

    return {
        "skills": skills_score,
        "experience": experience_score,
        "projects": projects_score,
        "overall": overall_score
    }


if __name__ == "__main__":

    sample_resume = {
        "skills": """
        Python, Flask, FastAPI, SQL, Machine Learning,
        REST APIs and Git.
        """,

        "experience": """
        Developed backend applications and REST APIs
        using Python and Flask. Worked on machine
        learning projects and data processing.
        """,

        "projects": """
        Built an AI-powered resume analyzer using
        Python, Streamlit and Google Gemini API.
        """
    }

    sample_job = {
        "skills": """
        Python, FastAPI, Machine Learning, SQL,
        REST APIs and Git.
        """,

        "experience": """
        Experience developing backend services,
        REST APIs and machine learning applications
        using Python.
        """,

        "projects": """
        Experience building AI applications,
        resume analysis systems and LLM-based projects.
        """
    }

    result = compare_resume_with_job(
        sample_resume,
        sample_job
    )

    print("\n======================================")
    print("SEMANTIC MATCHING ENGINE")
    print("======================================")

    for section, data in result.items():

        print(f"\n{section.upper()}")

        print(
            "Similarity:",
            data["similarity_percentage"],
            "%"
        )

        print(
            "Category:",
            data["category"]
        )