# Education & Certification Parsing Documentation

## 1. Overview

The Education & Certification Parsing module extracts academic qualifications and professional certifications from resumes and converts them into structured data.

The system is designed for AI-based recruitment and resume screening applications.

## 2. Education Extraction

The education parser identifies:

- Degree type
- Field of study
- Institution
- Graduation year

Supported degree examples include:

- Bachelor of Computer Applications
- Master of Computer Applications
- Bachelor of Technology
- Master of Technology
- Bachelor of Science
- Master of Science
- Master of Business Administration
- Doctor of Philosophy

The parser also normalizes different degree naming conventions into standard names.

## 3. Certification Extraction

The certification parser identifies professional certifications from resume text.

Examples:

- Google Data Analytics Certificate
- AWS Certified Cloud Practitioner
- Microsoft Certified: Azure Fundamentals
- TensorFlow Developer Certificate
- PMP
- CompTIA Security+

Certification names are normalized where applicable.

## 4. Certification Relevance Categories

Certifications are categorized into the following groups:

- AI / Machine Learning
- Data Analytics
- Cloud
- Programming
- Cybersecurity
- Project Management
- Database

This allows recruitment systems to understand the relevance of certifications to different job roles.

## 5. Education Relevance Logic

The relevance scorer compares the candidate's education with the target job role.

Example:

Target Role:

AI Engineer

Relevant education fields include:

- Computer Science
- Computer Applications
- Artificial Intelligence
- Machine Learning
- Data Science
- Information Technology
- Software Engineering

## 6. Relevance Scoring

The system assigns a relevance score based on the relationship between the candidate's education and the target role.

Scoring categories:

| Score | Category |
|---|---|
| 80–100 | Highly Relevant |
| 50–79 | Relevant |
| 25–49 | Partially Relevant |
| 0–24 | Low Relevance |

## 7. Structured Output

The final output is stored in:

`output/structured_academic_profile.json`

The structured profile contains:

- Resume ID
- Target role
- Education details
- Certification details
- Education relevance score
- Education relevance category

## 8. Testing

Unit tests were implemented to validate:

- Degree extraction
- Institution extraction
- Graduation year extraction
- Certification extraction
- Certification categorization
- Education relevance scoring
- Relevance category classification

The test suite successfully validates the core functionality of the module.

## 9. Limitations

The current implementation is a rule-based prototype.

Possible limitations include:

- Complex resume layouts may affect extraction.
- Unusual degree names may not be recognized.
- Certifications written in uncommon formats may not be detected.
- Relevance scoring is based on predefined role keywords.

## 10. Future Improvements

The system can be improved by adding:

- NLP-based education entity extraction
- Machine learning-based classification
- More degree and certification aliases
- OCR support for scanned resumes
- Advanced semantic similarity
- Integration with the complete ATS pipeline

## 11. Conclusion

The Education & Certification Parsing module successfully converts academic and certification information from resumes into structured, AI-readable profiles and evaluates education relevance against target job roles.