import unittest

from experience_parser import (
    parse_experience,
    calculate_total_experience,
    detect_gaps,
    detect_overlaps
)


class TestExperienceParser(unittest.TestCase):

    def setUp(self):

        self.resume_text = """
        Python Developer
        ABC Technologies
        January 2024 - June 2024

        AI Engineer
        XYZ Solutions
        July 2024 - December 2025
        """

    def test_experience_extraction(self):

        experiences = parse_experience(
            self.resume_text
        )

        self.assertEqual(
            len(experiences),
            2
        )

    def test_job_title_extraction(self):

        experiences = parse_experience(
            self.resume_text
        )

        self.assertEqual(
            experiences[0]["job_title"],
            "Python Developer"
        )

    def test_company_extraction(self):

        experiences = parse_experience(
            self.resume_text
        )

        self.assertEqual(
            experiences[0]["company"],
            "ABC Technologies"
        )

    def test_total_experience(self):

        experiences = parse_experience(
            self.resume_text
        )

        total_months = calculate_total_experience(
            experiences
        )

        self.assertEqual(
            total_months,
            22
        )

    def test_no_gap_between_jobs(self):

        experiences = parse_experience(
            self.resume_text
        )

        gaps = detect_gaps(
            experiences
        )

        self.assertEqual(
            len(gaps),
            0
        )

    def test_no_overlap_between_jobs(self):

        experiences = parse_experience(
            self.resume_text
        )

        overlaps = detect_overlaps(
            experiences
        )

        self.assertEqual(
            len(overlaps),
            0
        )


if __name__ == "__main__":
    unittest.main()