import re
from skill_dictionary import SKILL_DICTIONARY, SKILL_STACKS


def normalize_text(text):
    """Clean and normalize resume text."""
    text = text.lower()
    text = text.replace("–", "-")
    text = text.replace("—", "-")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_confidence(skill, matched_text, context):
    """
    Calculate confidence score for an extracted skill.

    Higher confidence is given when:
    - The skill appears as an exact match.
    - The skill appears in a skills-related context.
    """

    score = 0.80

    if skill.lower() == matched_text.lower():
        score += 0.10

    skill_context_words = [
        "skills",
        "technical skills",
        "technologies",
        "tools",
        "expertise",
        "proficient",
        "experienced",
        "knowledge"
    ]

    if any(word in context for word in skill_context_words):
        score += 0.08

    return min(round(score, 2), 0.99)


def expand_skill_stacks(text):
    """Expand common technology stacks such as MERN and MEAN."""

    expanded_skills = []

    for stack, skills in SKILL_STACKS.items():
        pattern = rf"\b{re.escape(stack)}\b"

        if re.search(pattern, text, re.IGNORECASE):
            expanded_skills.extend(skills)

    return expanded_skills


def extract_skills(text):
    """
    Extract and normalize skills from resume text.

    Returns:
        List of structured skill objects.
    """

    normalized_text = normalize_text(text)

    extracted = {}

    for category, skills in SKILL_DICTIONARY.items():

        for canonical_skill, synonyms in skills.items():

            all_terms = [canonical_skill] + synonyms

            for term in all_terms:

                escaped_term = re.escape(term.lower())

                pattern = rf"(?<!\w){escaped_term}(?!\w)"

                match = re.search(pattern, normalized_text)

                if match:

                    start = max(0, match.start() - 60)
                    end = min(len(normalized_text), match.end() + 60)

                    context = normalized_text[start:end]

                    confidence = calculate_confidence(
                        canonical_skill,
                        match.group(),
                        context
                    )

                    if canonical_skill not in extracted:
                        extracted[canonical_skill] = {
                            "skill": canonical_skill,
                            "category": category,
                            "confidence": confidence,
                            "matched_as": match.group()
                        }

                    else:
                        # Keep the highest confidence score
                        extracted[canonical_skill]["confidence"] = max(
                            extracted[canonical_skill]["confidence"],
                            confidence
                        )

    # Expand technology stacks
    stack_skills = expand_skill_stacks(normalized_text)

    for skill in stack_skills:

        # Find category for expanded skill
        category = "Technical"

        for cat, skills in SKILL_DICTIONARY.items():
            if skill in skills:
                category = cat
                break

        if skill not in extracted:
            extracted[skill] = {
                "skill": skill,
                "category": category,
                "confidence": 0.85,
                "matched_as": "skill stack"
            }

    # Deduplicate and sort
    results = list(extracted.values())

    results.sort(
        key=lambda item: (-item["confidence"], item["skill"])
    )

    return results