# Day 13 – ATS Scoring Engine

## Objective

Design a transparent and explainable ATS scoring framework for evaluating candidates against job requirements.

## Features

- Skill match scoring
- Experience relevance scoring
- Education alignment scoring
- Semantic similarity scoring
- Configurable role-based weights
- Final candidate score generation
- Explainable scoring output
- Missing data handling
- JSON candidate score generation
- Unit testing

## Scoring Parameters

The ATS score is calculated using four parameters:

| Parameter | Default Weight |
|---|---:|
| Skill Match | 40% |
| Experience Relevance | 25% |
| Education Alignment | 15% |
| Semantic Similarity | 20% |
| Total | 100% |

## Dynamic Weight System

The system supports role-specific scoring weights for:

- AI Engineer
- Python Developer
- Data Analyst
- Java Backend Developer

A default weight configuration is used when an unknown role is provided.

## Scoring Categories

| Score | Category |
|---|---|
| 80–100 | Strong Match |
| 65–79.99 | Good Match |
| 50–64.99 | Moderate Match |
| Below 50 | Low Match |

## Project Structure

```text
Day_13_ATS_Scoring_Engine/
│
├── main.py
├── scoring_engine.py
├── weight_config.py
├── explainable_output.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── candidate_profile.json
│   └── job_requirements.json
│
├── output/
│   └── candidate_score.json
│
├── tests/
│   └── test_ats_scoring.py
│
└── documentation/
    └── scoring_formula.md