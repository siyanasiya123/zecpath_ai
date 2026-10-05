import unittest

from skill_extractor import extract_skills


class TestSkillExtractor(unittest.TestCase):

    def test_python_skill(self):
        text = "Experienced Python developer."
        skills = extract_skills(text)

        skill_names = [skill["skill"] for skill in skills]

        self.assertIn("python", skill_names)

    def test_synonym_detection(self):
        text = "Experienced in JS and ReactJS."
        skills = extract_skills(text)

        skill_names = [skill["skill"] for skill in skills]

        self.assertIn("javascript", skill_names)
        self.assertIn("react", skill_names)

    def test_skill_stack(self):
        text = "Experienced MERN developer."
        skills = extract_skills(text)

        skill_names = [skill["skill"] for skill in skills]

        self.assertIn("mongodb", skill_names)
        self.assertIn("express.js", skill_names)
        self.assertIn("react", skill_names)
        self.assertIn("node.js", skill_names)

    def test_deduplication(self):
        text = "Python Python Python developer."
        skills = extract_skills(text)

        skill_names = [skill["skill"] for skill in skills]

        self.assertEqual(skill_names.count("python"), 1)

    def test_confidence_score(self):
        text = "Python developer with machine learning experience."
        skills = extract_skills(text)

        for skill in skills:
            self.assertGreaterEqual(skill["confidence"], 0.80)
            self.assertLessEqual(skill["confidence"], 0.99)


if __name__ == "__main__":
    unittest.main()