import unittest

from weight_config import (
    get_weights,
    validate_weights
)

from scoring_engine import (
    calculate_skill_match,
    calculate_experience_relevance,
    calculate_education_alignment,
    calculate_semantic_similarity,
    calculate_final_score,
    get_score_category,
    generate_candidate_score
)


class TestATSScoring(unittest.TestCase):

    def test_weight_configuration(self):
        weights = get_weights("AI Engineer")

        self.assertEqual(
            weights["skill_match"],
            0.40
        )

        self.assertTrue(
            validate_weights(weights)
        )

    def test_skill_match(self):
        candidate_skills = [
            "Python",
            "SQL",
            "Machine Learning"
        ]

        required_skills = [
            "Python",
            "SQL",
            "Machine Learning",
            "Docker"
        ]

        score = calculate_skill_match(
            candidate_skills,
            required_skills
        )

        self.assertEqual(
            score,
            75.0
        )

    def test_experience_relevance(self):
        score = calculate_experience_relevance(
            2,
            2
        )

        self.assertEqual(
            score,
            100.0
        )

    def test_education_alignment(self):
        score = calculate_education_alignment(
            "MCA",
            "MCA"
        )

        self.assertEqual(
            score,
            100.0
        )

    def test_semantic_similarity(self):
        score = calculate_semantic_similarity(
            0.86
        )

        self.assertEqual(
            score,
            86.0
        )

    def test_score_category(self):
        self.assertEqual(
            get_score_category(90),
            "Strong Match"
        )

        self.assertEqual(
            get_score_category(70),
            "Good Match"
        )

        self.assertEqual(
            get_score_category(55),
            "Moderate Match"
        )

        self.assertEqual(
            get_score_category(40),
            "Low Match"
        )

    def test_final_score(self):

        score = calculate_final_score(
            80,
            100,
            100,
            86,
            "AI Engineer"
        )

        self.assertEqual(
            score,
            88.2
        )

    def test_complete_candidate_score(self):

        candidate = {
            "skills": [
                "Python",
                "FastAPI",
                "Machine Learning",
                "SQL"
            ],
            "experience_years": 2,
            "education": "MCA",
            "semantic_similarity": 0.86
        }

        job = {
            "role": "AI Engineer",
            "required_skills": [
                "Python",
                "FastAPI",
                "Machine Learning",
                "SQL",
                "Docker"
            ],
            "required_experience_years": 2,
            "required_education": "MCA"
        }

        result = generate_candidate_score(
            candidate,
            job
        )

        self.assertIn(
            "final_score",
            result
        )

        self.assertIn(
            "category",
            result
        )

        self.assertGreaterEqual(
            result["final_score"],
            0
        )

        self.assertLessEqual(
            result["final_score"],
            100
        )


if __name__ == "__main__":
    unittest.main()