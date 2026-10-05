import unittest

from education_parser import (
    parse_education,
    detect_degree,
    extract_graduation_year
)

from certification_parser import (
    parse_certifications,
    categorize_certification
)

from relevance_scorer import (
    calculate_education_relevance,
    get_relevance_category
)


class TestEducationCertification(unittest.TestCase):

    def test_degree_extraction(self):
        text = "Master of Computer Applications in Computer Applications"
        degree = detect_degree(text)

        self.assertEqual(
            degree,
            "Master of Computer Applications"
        )

    def test_institution_extraction(self):
        text = """
        EDUCATION
        Master of Computer Applications in Computer Applications
        University of Calicut
        2026
        """

        education = parse_education(text)

        self.assertEqual(
            education[0]["institution"],
            "University of Calicut"
        )

    def test_graduation_year(self):
        text = "Bachelor of Computer Applications\nABC College\n2024"

        year = extract_graduation_year(text)

        self.assertEqual(year, 2024)

    def test_certification_extraction(self):
        text = """
        CERTIFICATIONS
        Google Data Analytics Certificate
        AWS Certified Cloud Practitioner
        """

        certifications = parse_certifications(text)

        self.assertEqual(
            len(certifications),
            2
        )

    def test_certification_category(self):
        category = categorize_certification(
            "AWS Certified Cloud Practitioner"
        )

        self.assertEqual(
            category,
            "Cloud"
        )

    def test_relevance_score(self):
        education = [
            {
                "degree": "Master of Computer Applications",
                "field_of_study": "Computer Applications",
                "institution": "University of Calicut",
                "graduation_year": 2026
            }
        ]

        score = calculate_education_relevance(
            education,
            "AI Engineer"
        )

        self.assertEqual(score, 100)

    def test_relevance_category(self):
        category = get_relevance_category(100)

        self.assertEqual(
            category,
            "Highly Relevant"
        )


if __name__ == "__main__":
    unittest.main()