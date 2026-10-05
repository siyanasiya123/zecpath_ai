# Day 8 – Resume Section Segmentation

## Project Overview
This project automatically identifies and separates major sections
of a resume using rule-based heading detection and text classification.

## Objectives
- Detect resume section headings.
- Classify Skills, Work Experience, Education,
  Certifications, and Projects.
- Handle different heading variations.
- Generate structured JSON output.
- Test section detection accuracy.

## Technologies Used
- Python
- Regular Expressions
- JSON
- Unittest

## Project Structure
- main.py – Main program
- section_classifier.py – Section classification logic
- data/ – Sample resume data
- output/ – Labeled resume output
- tests/ – Unit tests
- documentation/ – Accuracy report

## How to Run
1. Open the project folder in VS Code.
2. Run: python main.py
3. Run tests: python -m unittest discover -s tests -v

## Test Results
- Total tests: 7
- Passed: 7
- Failed: 0

## Limitations
The current implementation uses rule-based heading detection.
Complex tables, columns, and resumes with missing headings
may require additional processing.

## Deliverables
1. Resume Section Classifier Module
2. Labeled Resume Samples
3. Section Detection Accuracy Report