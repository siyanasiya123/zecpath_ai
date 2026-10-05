import re


# -------------------------------------------------
# Certification Categories
# -------------------------------------------------

CERTIFICATION_CATEGORIES = {

    "AI / Machine Learning": [
        "machine learning",
        "artificial intelligence",
        "deep learning",
        "generative ai",
        "tensorflow",
        "pytorch",
        "natural language processing",
        "nlp"
    ],

    "Data Analytics": [
        "data analytics",
        "data analysis",
        "google data analytics",
        "power bi",
        "tableau",
        "data analyst",
        "business intelligence"
    ],

    "Cloud": [
        "aws",
        "amazon web services",
        "azure",
        "microsoft azure",
        "google cloud",
        "gcp",
        "cloud practitioner"
    ],

    "Programming": [
        "python",
        "java",
        "javascript",
        "programming",
        "web development"
    ],

    "Cybersecurity": [
        "cybersecurity",
        "cyber security",
        "ethical hacking",
        "network security",
        "information security",
        "security+"
    ],

    "Project Management": [
        "project management",
        "pmp",
        "scrum",
        "agile",
        "product management"
    ],

    "Database": [
        "sql",
        "mysql",
        "oracle",
        "database"
    ]
}


# -------------------------------------------------
# Certification Name Normalization
# -------------------------------------------------

CERTIFICATION_ALIASES = {

    "aws certified cloud practitioner":
        "AWS Certified Cloud Practitioner",

    "aws cloud practitioner":
        "AWS Certified Cloud Practitioner",

    "amazon web services cloud practitioner":
        "AWS Certified Cloud Practitioner",

    "google data analytics certificate":
        "Google Data Analytics Certificate",

    "microsoft certified azure fundamentals":
        "Microsoft Certified: Azure Fundamentals",

    "azure fundamentals":
        "Microsoft Certified: Azure Fundamentals",

    "pmp":
        "Project Management Professional (PMP)",

    "project management professional":
        "Project Management Professional (PMP)",

    "comptia security+":
        "CompTIA Security+",

    "security+":
        "CompTIA Security+"
}


# -------------------------------------------------
# Normalize Certification Name
# -------------------------------------------------

def normalize_certification(name):
    """
    Convert different certification names
    into standardized names.
    """

    clean_name = name.strip()

    # Remove unnecessary spaces
    clean_name = re.sub(
        r"\s+",
        " ",
        clean_name
    )

    lookup_name = clean_name.lower()

    if lookup_name in CERTIFICATION_ALIASES:
        return CERTIFICATION_ALIASES[lookup_name]

    return clean_name


# -------------------------------------------------
# Categorize Certification
# -------------------------------------------------

def categorize_certification(name):
    """
    Assign a relevance category to a certification.
    """

    lower_name = name.lower()

    for category, keywords in CERTIFICATION_CATEGORIES.items():

        for keyword in keywords:

            if keyword in lower_name:
                return category

    return "Other"


# -------------------------------------------------
# Detect Certification Lines
# -------------------------------------------------

def is_certification_line(line):
    """
    Determine whether a line likely contains
    a professional certification.
    """

    lower_line = line.lower()

    certification_keywords = [
        "certified",
        "certification",
        "certificate",
        "credential",
        "pmp",
        "security+",
        "aws",
        "azure",
        "google cloud",
        "gcp"
    ]

    return any(
        keyword in lower_line
        for keyword in certification_keywords
    )


# -------------------------------------------------
# Parse Certifications
# -------------------------------------------------

def parse_certifications(text):
    """
    Extract and structure certifications
    from resume text.
    """

    certifications = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    inside_certification_section = False

    for line in lines:

        lower_line = line.lower()

        # Detect certification section
        if (
            "certification" in lower_line
            or "certifications" in lower_line
        ):

            inside_certification_section = True
            continue

        # Stop when another resume section starts
        if inside_certification_section and any(
            section in lower_line
            for section in [
                "education",
                "experience",
                "skills",
                "projects",
                "achievements",
                "languages",
                "summary",
                "profile"
            ]
        ):

            inside_certification_section = False
            continue

        # Detect certification
        if is_certification_line(line):

            certification_name = line

            # Remove bullet symbols
            certification_name = re.sub(
                r"^[•\-\*\d\.\)\s]+",
                "",
                certification_name
            ).strip()

            if not certification_name:
                continue

            # Normalize name
            normalized_name = normalize_certification(
                certification_name
            )

            # Categorize certification
            category = categorize_certification(
                normalized_name
            )

            certification_object = {
                "name": normalized_name,
                "category": category
            }

            # Avoid duplicates
            if certification_object not in certifications:
                certifications.append(
                    certification_object
                )

    return certifications


# -------------------------------------------------
# Main Test
# -------------------------------------------------

if __name__ == "__main__":

    sample_text = """
    CERTIFICATIONS

    Google Data Analytics Certificate
    AWS Certified Cloud Practitioner
    Microsoft Certified: Azure Fundamentals
    Python Programming Certificate
    """

    result = parse_certifications(
        sample_text
    )

    print("Certification Information:")

    for certification in result:
        print(certification)