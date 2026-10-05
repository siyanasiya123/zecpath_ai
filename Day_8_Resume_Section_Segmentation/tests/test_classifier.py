import sys
from pathlib import Path
import unittest

# Add the project folder to the Python path
PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from section_classifier import (
    classify_resume,
    detect_section_heading,
)


class TestResumeSectionClassifier(unittest.TestCase):

    def test_skills_heading(self):
        self.assertEqual(
            detect_section_heading("Skills"),
            "Skills"
        )

    def test_experience_heading(self):
        self.assertEqual(
            detect_section_heading("Work Experience"),
            "Work Experience"
        )

    def test_education_heading(self):
        self.assertEqual(
            detect_section_heading("Education"),
            "Education"
        )

    def test_certifications_heading(self):
        self.assertEqual(
            detect_section_heading("Certifications"),
            "Certifications"
        )

    def test_projects_heading(self):
        self.assertEqual(
            detect_section_heading("Projects"),
            "Projects"
        )

    def test_resume_classification(self):
        resume = """
        Skills
        Python, Flask, SQL

        Education
        MCA
        """

        result = classify_resume(resume)

        self.assertIn("Python, Flask, SQL", result["Skills"])
        self.assertIn("MCA", result["Education"])

    def test_unknown_heading_content(self):
        resume = """
        John Doe
        Software Developer
        """

        result = classify_resume(resume)

        self.assertIn("John Doe", result["Other"])


if __name__ == "__main__":
    unittest.main(verbosity=2)