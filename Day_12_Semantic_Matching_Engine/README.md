# Day 12 – Semantic Matching Engine

## Objective

Develop a semantic matching engine that compares resumes with job descriptions using AI-based text embeddings instead of simple keyword matching.

## Features

- Converts resume and job description text into semantic embeddings.
- Uses the `all-MiniLM-L6-v2` sentence transformer model.
- Calculates cosine similarity between resume and job description sections.
- Compares Skills, Experience and Projects.
- Generates an overall semantic matching score.
- Categorizes similarity into different relevance levels.
- Supports multiple resumes and job descriptions.
- Generates structured JSON matching results.

## Similarity Categories

| Similarity Score | Category |
|---|---|
| 0.80 – 1.00 | Highly Similar |
| 0.65 – 0.79 | Relevant |
| 0.50 – 0.64 | Partially Relevant |
| Below 0.50 | Low Similarity |

## Model

**Embedding Model:** all-MiniLM-L6-v2

**Embedding Dimension:** 384

## Project Structure

```text
Day_12_Semantic_Matching_Engine/
│
├── main.py
├── embedding_engine.py
├── similarity_scorer.py
├── matching_engine.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sample_resumes.txt
│   └── job_descriptions.txt
│
├── output/
│   └── semantic_matching_results.json
│
├── tests/
│   └── test_semantic_matching.py
│
└── documentation/
    └── matching_accuracy_report.md