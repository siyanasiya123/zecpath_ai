# Day 10 - Experience Parsing & Relevance Engine

## Objective

To analyze professional experience from resumes and calculate the relevance of previous roles to a target job role.

## Features

- Extracts company names
- Extracts job titles
- Extracts employment dates
- Calculates employment duration
- Calculates total professional experience
- Detects employment gaps
- Detects overlapping roles
- Calculates role relevance scores
- Generates structured JSON output
- Includes unit tests

## Project Structure

```text
Day_10_Experience_Parsing_Relevance_Engine/
│
├── main.py
├── experience_parser.py
├── relevance_scorer.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sample_resumes.txt
│   └── job_requirements.txt
│
├── output/
│   └── structured_experience_output.json
│
├── tests/
│   └── test_experience_parser.py
│
└── documentation/
    └── experience_relevance_documentation.md