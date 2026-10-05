import re
from datetime import date


MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}


def parse_date(value):
    """
    Convert different date formats into a date object.
    Supports:
    January 2024
    Jan 2024
    2024
    2024-01-01
    Present
    """

    if not value:
        return None

    value = value.strip().lower()

    # Present
    if value == "present":
        today = date.today()
        return date(today.year, today.month, 1)

    # ISO format: YYYY-MM-DD
    iso_match = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})$", value)

    if iso_match:
        year = int(iso_match.group(1))
        month = int(iso_match.group(2))
        day = int(iso_match.group(3))

        return date(year, month, day)

    # Month + Year
    month_year_match = re.search(
        r"(january|february|march|april|may|june|july|"
        r"august|september|october|november|december|"
        r"jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec)"
        r"\s+(\d{4})",
        value
    )

    if month_year_match:

        month_name = month_year_match.group(1)
        year = int(month_year_match.group(2))

        month_abbreviations = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "sept": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12
        }

        if month_name in MONTHS:
            month = MONTHS[month_name]
        else:
            month = month_abbreviations[month_name]

        return date(year, month, 1)

    # Year only
    year_match = re.search(r"\b(\d{4})\b", value)

    if year_match:
        year = int(year_match.group(1))
        return date(year, 1, 1)

    return None


def calculate_months(start_date, end_date):
    """
    Calculate the number of elapsed months between two dates.
    """

    if not start_date or not end_date:
        return 0

    return (
        (end_date.year - start_date.year) * 12
        + (end_date.month - start_date.month)
    )


def parse_experience(text):
    """
    Extract job title, company, start date,
    end date and duration from resume text.
    """

    experiences = []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    date_pattern = re.compile(
        r"("
        r"(?:January|February|March|April|May|June|July|August|"
        r"September|October|November|December|"
        r"Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)"
        r"\s+\d{4}"
        r"|"
        r"\d{4}"
        r")"
        r"\s*(?:-|–|—|to)\s*"
        r"(Present|"
        r"(?:January|February|March|April|May|June|July|August|"
        r"September|October|November|December|"
        r"Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)"
        r"\s+\d{4}"
        r"|\d{4})",
        re.IGNORECASE
    )

    job_keywords = [
        "developer",
        "engineer",
        "analyst",
        "intern",
        "manager",
        "consultant",
        "designer",
        "specialist",
        "scientist",
        "administrator",
        "associate"
    ]

    for index, line in enumerate(lines):

        match = date_pattern.search(line)

        if not match:
            continue

        start_date = match.group(1)
        end_date = match.group(2)

        job_title = ""
        company = ""

        # Look at previous lines to identify job title and company
        previous_lines = lines[max(0, index - 2):index]

        for previous_line in reversed(previous_lines):

            lower_line = previous_line.lower()

            if any(
                keyword in lower_line
                for keyword in job_keywords
            ):
                job_title = previous_line
                break

        for previous_line in previous_lines:

            if previous_line != job_title:
                company = previous_line
                break

        # If company is still empty
        if not company and index > 0:
            company = lines[index - 1]

        start = parse_date(start_date)

        if end_date.lower() == "present":
            end = parse_date("present")
        else:
            end = parse_date(end_date)

        duration_months = calculate_months(
            start,
            end
        )

        experiences.append({
            "job_title": job_title,
            "company": company,
            "start_date": start.isoformat() if start else None,
            "end_date": end.isoformat() if end else None,
            "duration_months": duration_months
        })

    return experiences


def calculate_total_experience(experiences):
    """
    Calculate total professional experience in months.
    """

    total_months = 0

    for experience in experiences:

        total_months += experience.get(
            "duration_months",
            0
        )

    return total_months


def detect_gaps(experiences):
    """
    Detect gaps between consecutive employment periods.
    """

    if len(experiences) < 2:
        return []

    sorted_experiences = sorted(
        experiences,
        key=lambda x: x["start_date"] or ""
    )

    gaps = []

    for current, next_experience in zip(
        sorted_experiences,
        sorted_experiences[1:]
    ):

        if not current["end_date"]:
            continue

        if not next_experience["start_date"]:
            continue

        current_end = parse_date(
            current["end_date"]
        )

        next_start = parse_date(
            next_experience["start_date"]
        )

        if not current_end or not next_start:
            continue

        gap_months = calculate_months(
            current_end,
            next_start
        )

        # Consecutive months are not considered a gap
        if gap_months > 1:

            actual_gap = gap_months - 1

            gaps.append({
                "from": current["end_date"],
                "to": next_experience["start_date"],
                "gap_months": actual_gap
            })

    return gaps


def detect_overlaps(experiences):
    """
    Detect overlapping employment periods.
    """

    overlaps = []

    for i in range(len(experiences)):

        for j in range(i + 1, len(experiences)):

            first = experiences[i]
            second = experiences[j]

            if not first["start_date"] or not first["end_date"]:
                continue

            if not second["start_date"] or not second["end_date"]:
                continue

            first_start = parse_date(
                first["start_date"]
            )

            first_end = parse_date(
                first["end_date"]
            )

            second_start = parse_date(
                second["start_date"]
            )

            second_end = parse_date(
                second["end_date"]
            )

            if not all([
                first_start,
                first_end,
                second_start,
                second_end
            ]):
                continue

            # Check actual overlap
            if (
                first_start < second_end
                and second_start < first_end
            ):

                overlaps.append({
                    "role_1": first["job_title"],
                    "role_2": second["job_title"],
                    "company_1": first["company"],
                    "company_2": second["company"]
                })

    return overlaps