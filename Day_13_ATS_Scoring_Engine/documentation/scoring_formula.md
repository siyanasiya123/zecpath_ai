# Day 13 – ATS Scoring Formula Design

## 1. Objective

The objective of this module is to design a transparent and explainable ATS scoring framework for evaluating candidates against job requirements.

The system calculates an overall candidate score using:

- Skill Match
- Experience Relevance
- Education Alignment
- Semantic Similarity

## 2. Scoring Formula

The final ATS score is calculated using a weighted scoring formula:

Final ATS Score =
(Skill Match × Skill Weight)
+
(Experience Relevance × Experience Weight)
+
(Education Alignment × Education Weight)
+
(Semantic Similarity × Semantic Weight)

The final score is represented on a scale of 0–100.

## 3. Default Weights

| Parameter | Weight |
|---|---:|
| Skill Match | 40% |
| Experience Relevance | 25% |
| Education Alignment | 15% |
| Semantic Similarity | 20% |
| Total | 100% |

## 4. Role-Based Dynamic Weights

The system supports different weights for different job roles.

### AI Engineer

- Skill Match: 40%
- Experience Relevance: 25%
- Education Alignment: 15%
- Semantic Similarity: 20%

### Python Developer

- Skill Match: 40%
- Experience Relevance: 30%
- Education Alignment: 10%
- Semantic Similarity: 20%

### Data Analyst

- Skill Match: 35%
- Experience Relevance: 25%
- Education Alignment: 20%
- Semantic Similarity: 20%

### Java Backend Developer

- Skill Match: 40%
- Experience Relevance: 30%
- Education Alignment: 10%
- Semantic Similarity: 20%

## 5. Skill Match

Skill Match measures how many required job skills are present in the candidate profile.

Formula:

Skill Match =
(Matched Skills / Required Skills) × 100

Example:

Required skills = 5

Matched skills = 4

Skill Match = 80%

## 6. Experience Relevance

Experience Relevance compares the candidate's experience with the minimum experience required for the job.

Formula:

Experience Score =
(Candidate Experience / Required Experience) × 100

The score is capped at 100%.

## 7. Education Alignment

Education Alignment compares the candidate's education with the education requirement.

Scoring:

- Exact match → 100%
- Partial match → 80%
- No match → 0%

If education information is missing from the job requirement, the system assigns 100%.

## 8. Semantic Similarity

Semantic Similarity represents the similarity between candidate information and job requirements.

The similarity score is converted into a percentage:

Semantic Similarity =
Similarity Score × 100

For example:

Similarity Score = 0.86

Semantic Similarity = 86%

## 9. Candidate Categories

The final ATS score is classified into four categories:

| Score | Category |
|---|---|
| 80–100 | Strong Match |
| 65–79.99 | Good Match |
| 50–64.99 | Moderate Match |
| Below 50 | Low Match |

## 10. Missing Data Handling

The scoring engine is designed to handle missing information without crashing.

Examples:

- Missing candidate skills → Skill Match becomes 0%.
- Missing candidate experience → Experience score becomes 0%.
- Missing semantic similarity → Semantic score becomes 0%.
- Missing job education requirement → Education Alignment becomes 100%.
- Unknown job role → Default weights are used.

## 11. Explainable Output

The system provides a detailed score breakdown instead of returning only one final score.

Example:

```text
Skill Match: 80%
Experience Relevance: 100%
Education Alignment: 100%
Semantic Similarity: 86%

Final ATS Score: 88.2 / 100
Category: Strong Match