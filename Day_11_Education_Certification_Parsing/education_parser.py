import re


# -------------------------------------------------
# Degree Normalization
# -------------------------------------------------

DEGREE_ALIASES = {
    "mca": "Master of Computer Applications",
    "master of computer applications": "Master of Computer Applications",

    "bca": "Bachelor of Computer Applications",
    "bachelor of computer applications": "Bachelor of Computer Applications",

    "btech": "Bachelor of Technology",
    "b.tech": "Bachelor of Technology",
    "b.e": "Bachelor of Engineering",
    "be": "Bachelor of Engineering",

    "bsc": "Bachelor of Science",
    "b.sc": "Bachelor of Science",

    "msc": "Master of Science",
    "m.sc": "Master of Science",

    "mtech": "Master of Technology",
    "m.tech": "Master of Technology",

    "mba": "Master of Business Administration",
    "master of business administration": "Master of Business Administration",

    "phd": "Doctor of Philosophy",
    "ph.d": "Doctor of Philosophy"
}


# -------------------------------------------------
# Normalize Degree Name
# -------------------------------------------------

def normalize_degree(degree):
    """
    Convert different degree naming conventions
    into a standard degree name.
    """

    degree_clean = degree.strip().lower()

    # Remove unnecessary punctuation
    degree_clean = degree_clean.replace(",", "")
    degree_clean = degree_clean.strip()

    if degree_clean in DEGREE_ALIASES:
        return DEGREE_ALIASES[degree_clean]

    return degree.strip()


# -------------------------------------------------
# Extract Graduation Year
# -------------------------------------------------

def extract_graduation_year(text):
    """
    Extract a four-digit graduation year.
    """

    year_matches = re.findall(
        r"\b(19\d{2}|20\d{2})\b",
        text
    )

    if year_matches:
        return int(year_matches[-1])

    return None


# -------------------------------------------------
# Detect Degree
# -------------------------------------------------

def detect_degree(line):
    """
    Detect and normalize degree names from a line.
    """

    lower_line = line.lower()

    # Check longer names first
    degree_patterns = [
        (
            r"master\s+of\s+computer\s+applications",
            "Master of Computer Applications"
        ),
        (
            r"master\s+of\s+business\s+administration",
            "Master of Business Administration"
        ),
        (
            r"bachelor\s+of\s+computer\s+applications",
            "Bachelor of Computer Applications"
        ),
        (
            r"bachelor\s+of\s+technology",
            "Bachelor of Technology"
        ),
        (
            r"bachelor\s+of\s+engineering",
            "Bachelor of Engineering"
        ),
        (
            r"master\s+of\s+technology",
            "Master of Technology"
        ),
        (
            r"master\s+of\s+science",
            "Master of Science"
        ),
        (
            r"bachelor\s+of\s+science",
            "Bachelor of Science"
        ),
        (
            r"\bm\.?c\.?a\.?\b",
            "Master of Computer Applications"
        ),
        (
            r"\bb\.?c\.?a\.?\b",
            "Bachelor of Computer Applications"
        ),
        (
            r"\bm\.?tech\.?\b",
            "Master of Technology"
        ),
        (
            r"\bb\.?tech\.?\b",
            "Bachelor of Technology"
        ),
        (
            r"\bb\.?e\.?\b",
            "Bachelor of Engineering"
        ),
        (
            r"\bm\.?sc\.?\b",
            "Master of Science"
        ),
        (
            r"\bb\.?sc\.?\b",
            "Bachelor of Science"
        ),
        (
            r"\bm\.?b\.?a\.?\b",
            "Master of Business Administration"
        ),
        (
            r"\bph\.?d\.?\b",
            "Doctor of Philosophy"
        )
    ]

    for pattern, normalized_degree in degree_patterns:

        if re.search(pattern, lower_line):
            return normalized_degree

    return None


# -------------------------------------------------
# Extract Field of Study
# -------------------------------------------------

def extract_field_of_study(line, degree):
    """
    Extract field of study from common formats.
    """

    patterns = [
        r"(?:in|major\s+in|specialization\s+in)\s+(.+)",
        r"(?:-\s*)(.+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            line,
            re.IGNORECASE
        )

        if match:

            field = match.group(1).strip()

            # Remove graduation year
            field = re.sub(
                r"\b(19\d{2}|20\d{2})\b",
                "",
                field
            ).strip()

            if field:
                return field

    # If degree itself is the field
    if degree == "Master of Computer Applications":
        return "Computer Applications"

    if degree == "Bachelor of Computer Applications":
        return "Computer Applications"

    if degree == "Bachelor of Technology":
        return "Technology"

    if degree == "Bachelor of Engineering":
        return "Engineering"

    if degree == "Master of Technology":
        return "Technology"

    if degree == "Master of Science":
        return "Science"

    if degree == "Bachelor of Science":
        return "Science"

    return "Not Specified"


# -------------------------------------------------
# Extract Institution
# -------------------------------------------------

def extract_institution(lines, current_index):
    """
    Identify the institution from nearby lines.
    """

    institution_keywords = [
        "university",
        "college",
        "institute",
        "school",
        "academy"
    ]

    # Look at the next two lines
    nearby_lines = lines[
        current_index + 1:
        current_index + 3
    ]

    for line in nearby_lines:

        lower_line = line.lower()

        if any(
            keyword in lower_line
            for keyword in institution_keywords
        ):

            # Remove year if present
            institution = re.sub(
                r"\b(19\d{2}|20\d{2})\b",
                "",
                line
            ).strip()

            return institution

    return "Not Specified"


# -------------------------------------------------
# Parse Education
# -------------------------------------------------

def parse_education(text):
    """
    Extract structured academic qualifications
    from resume text.
    """

    education = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    education_keywords = [
        "education",
        "academic",
        "qualification"
    ]

    inside_education_section = False

    for index, line in enumerate(lines):

        lower_line = line.lower()

        # Detect education section
        if any(
            keyword in lower_line
            for keyword in education_keywords
        ):

            inside_education_section = True
            continue

        # Detect another common resume section
        if inside_education_section and any(
            section in lower_line
            for section in [
                "experience",
                "skills",
                "projects",
                "certifications",
                "achievements",
                "languages"
            ]
        ):

            inside_education_section = False
            continue

        degree = detect_degree(line)

        if degree:

            graduation_year = extract_graduation_year(
                line
            )

            # Search nearby lines for graduation year
            if not graduation_year:

                nearby_text = " ".join(
                    lines[index:index + 3]
                )

                graduation_year = extract_graduation_year(
                    nearby_text
                )

            field_of_study = extract_field_of_study(
                line,
                degree
            )

            institution = extract_institution(
                lines,
                index
            )

            education.append({
                "degree": degree,
                "field_of_study": field_of_study,
                "institution": institution,
                "graduation_year": graduation_year
            })

    return education


# -------------------------------------------------
# Main Test
# -------------------------------------------------

if __name__ == "__main__":

    sample_text = """
    EDUCATION

    Master of Computer Applications in Computer Applications
    University of Calicut
    2026

    Bachelor of Computer Applications
    ABC College
    2024
    """

    result = parse_education(sample_text)

    print("Education Information:")
    print(result)