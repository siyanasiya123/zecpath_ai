import unittest

from embedding_engine import generate_embedding
from similarity_scorer import (
    calculate_similarity,
    similarity_percentage,
    get_similarity_category
)
from matching_engine import compare_resume_with_job


class TestSemanticMatching(unittest.TestCase):

    def test_embedding_generation(self):
        text = "Python developer with machine learning experience."

        embedding = generate_embedding(text)

        self.assertEqual(len(embedding), 384)

    def test_similarity_calculation(self):
        embedding_1 = [1.0, 0.0, 0.0]
        embedding_2 = [1.0, 0.0, 0.0]

        score = calculate_similarity(
            embedding_1,
            embedding_2
        )

        self.assertEqual(score, 1.0)

    def test_similarity_percentage(self):
        score = 0.85

        percentage = similarity_percentage(score)

        self.assertEqual(percentage, 85.0)

    def test_similarity_category(self):
        category = get_similarity_category(0.90)

        self.assertEqual(
            category,
            "Highly Similar"
        )

    def test_matching_engine(self):

        resume = {
            "skills": "Python, Flask, SQL, Machine Learning",
            "experience": "Python backend developer experience",
            "projects": "AI resume analyzer project"
        }

        job = {
            "skills": "Python, FastAPI, SQL, Machine Learning",
            "experience": "Python backend development experience",
            "projects": "AI application development"
        }

        result = compare_resume_with_job(
            resume,
            job
        )

        self.assertIn("skills", result)
        self.assertIn("experience", result)
        self.assertIn("projects", result)
        self.assertIn("overall", result)

    def test_matching_score_exists(self):

        resume = {
            "skills": "Python",
            "experience": "Backend development",
            "projects": "AI application"
        }

        job = {
            "skills": "Python",
            "experience": "Backend development",
            "projects": "AI application"
        }

        result = compare_resume_with_job(
            resume,
            job
        )

        self.assertIn(
            "similarity_score",
            result["overall"]
        )

        self.assertGreaterEqual(
            result["overall"]["similarity_score"],
            0.0
        )


if __name__ == "__main__":
    unittest.main()