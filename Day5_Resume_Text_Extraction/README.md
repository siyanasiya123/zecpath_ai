# Day 5 - Resume Text Extraction and Structuring

## Objective

The objective of this task is to extract text from resume PDF files, clean and normalize the extracted text, and convert the information into structured JSON format.

## Project Structure

```text
Day5_Resume_Text_Extraction/
│
├── data/
│   ├── resumes/
│   ├── structured/
│   └── final/
│
└── src/
    ├── main.py
    ├── extractor.py
    ├── pdf_reader.py
    ├── docx_reader.py
    ├── text_cleaner.py
    ├── text_normalizer.py
    └── __init__.py