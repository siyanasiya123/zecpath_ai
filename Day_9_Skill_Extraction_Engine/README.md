# Day 9 – Skill Extraction Engine

## Objective

The Skill Extraction Engine identifies technical, business, and
creative skills from resume text and converts them into structured
data.

## Features

- Master skill dictionary
- Technical, Business, and Creative skill categories
- Skill synonym handling
- Skill stack expansion
- Spelling variation handling
- Skill normalization
- Duplicate removal
- Confidence scoring
- Structured JSON output

## Project Structure

Day_9_Skill_Extraction_Engine/

├── main.py
├── skill_extractor.py
├── skill_dictionary.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_resumes.txt
│
├── output/
│   └── structured_skill_output.json
│
├── tests/
│   └── test_skill_extractor.py
│
└── documentation/
    └── skill_confidence_scoring.md

## Technologies

- Python
- Regular Expressions
- JSON
- Standard Python Library

## How to Run

```bash
python main.py