import re
from typing import List, Dict, Any


SKILL_SYNONYMS = {
    "python": ["python", "python programming"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "natural language processing": [
        "natural language processing", "nlp"
    ],
    "sql": ["sql", "structured query language"],
    "flask": ["flask"],
    "fastapi": ["fastapi", "fast api"],
    "streamlit": ["streamlit"],
    "data analysis": ["data analysis", "data analytics"],
    "power bi": ["power bi", "powerbi"],
    "excel": ["excel", "microsoft excel"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "generative ai": ["generative ai", "gen ai"],
    "large language models": [
        "large language models", "llm", "llms"
    ],
    "rest api": ["rest api", "restful api", "rest apis"],
    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "js"],
    "java": ["java"],
    "c++": ["c++"],
    "aws": ["aws", "amazon web services"],
    "git": ["git", "github"]
}


ROLE_SYNONYMS = {
    "data analyst": [
        "data analyst", "data analytics specialist"
    ],
    "data scientist": [
        "data scientist", "data science specialist"
    ],
    "machine learning engineer": [
        "machine learning engineer", "ml engineer"
    ],
    "ai engineer": [
        "ai engineer", "artificial intelligence engineer"
    ],
    "python developer": [
        "python developer", "python programmer"
    ],
    "backend developer": [
        "backend developer",
        "back-end developer",
        "back end developer"
    ],
    "software developer": [
        "software developer", "software engineer"
    ],
    "web developer": [
        "web developer", "website developer"
    ]
}


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_role(text: str) -> str:
    normalized = normalize_text(text)

    for role, variations in ROLE_SYNONYMS.items():
        for variation in variations:
            pattern = r"\b" + re.escape(variation) + r"\b"

            if re.search(pattern, normalized):
                return role.title()

    return "Not specified"


def extract_skills(text: str) -> List[str]:
    normalized = normalize_text(text)
    found_skills = []

    for skill, variations in SKILL_SYNONYMS.items():
        for variation in variations:
            pattern = (
                r"(?<!\w)" + re.escape(variation) + r"(?!\w)"
            )

            if re.search(pattern, normalized):
                found_skills.append(skill)
                break

    return sorted(set(found_skills))


def extract_experience(text: str) -> Dict[str, Any]:
    normalized = normalize_text(text)

    range_pattern = (
        r"(\d+)\s*(?:-|to)\s*(\d+)\s*"
        r"(?:years?|yrs?)"
    )

    match = re.search(range_pattern, normalized)

    if match:
        return {
            "minimum_years": int(match.group(1)),
            "maximum_years": int(match.group(2))
        }

    single_pattern = (
        r"(\d+)\+?\s*(?:years?|yrs?)\s+"
        r"(?:of\s+)?(?:experience|exp)"
    )

    match = re.search(single_pattern, normalized)

    if match:
        years = int(match.group(1))
        return {
            "minimum_years": years,
            "maximum_years": None
        }

    return {
        "minimum_years": None,
        "maximum_years": None
    }


def extract_education(text: str) -> List[str]:
    normalized = normalize_text(text)

    qualifications = {
        "PhD": ["phd", "ph.d"],
        "Master's Degree": [
            "master's degree", "masters degree",
            "m.tech", "mca", "mba", "m.sc", "msc"
        ],
        "Bachelor's Degree": [
            "bachelor's degree", "bachelors degree",
            "b.tech", "b.e.", "bca", "b.sc",
            "bsc", "b.com"
        ],
        "Diploma": ["diploma"]
    }

    found = []

    for qualification, variations in qualifications.items():
        for variation in variations:
            pattern = (
                r"(?<!\w)" + re.escape(variation) + r"(?!\w)"
            )

            if re.search(pattern, normalized):
                found.append(qualification)
                break

    return found


def parse_job_description(text: str) -> Dict[str, Any]:
    if not text or not text.strip():
        raise ValueError("Job description cannot be empty.")

    return {
        "job_role": extract_role(text),
        "required_skills": extract_skills(text),
        "experience": extract_experience(text),
        "education": extract_education(text),
        "normalized_description": normalize_text(text)
    }