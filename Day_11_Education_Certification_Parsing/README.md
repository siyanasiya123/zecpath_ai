# Day 11 – Education & Certification Parsing

## Objective

Develop an AI-ready module to extract academic qualifications and professional certifications from resumes.

## Features

- Extracts degree type
- Extracts field of study
- Extracts institution name
- Extracts graduation year
- Extracts professional certifications
- Normalizes education and certification names
- Categorizes certifications by relevance
- Calculates education relevance for a target job role
- Generates structured JSON output
- Includes unit testing

## Project Structure

```text
Day_11_Education_Certification_Parsing/
│
├── main.py
├── education_parser.py
├── certification_parser.py
├── relevance_scorer.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sample_resumes.txt
│   └── job_requirements.txt
│
├── output/
│   └── structured_academic_profile.json
│
├── tests/
│   └── test_education_certification.py
│
└── documentation/
    └── education_certification_documentation.md