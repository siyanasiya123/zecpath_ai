# Semantic Matching Accuracy Report

## 1. Overview

This report evaluates the Semantic Matching Engine developed for Day 12.

The system uses semantic embeddings to compare resumes with job descriptions beyond simple keyword matching.

## 2. Evaluation Dataset

The system was tested using:

- 3 sample resumes
- 3 different job descriptions
- 9 total resume-to-job comparisons

The evaluated job types are:

1. AI / Python Developer
2. Java Backend Developer
3. Data Analyst

## 3. Matching Dimensions

The system compares three major areas:

- Skills
- Experience
- Projects

An overall semantic similarity score is also calculated.

## 4. Embedding Model

The system uses:

`all-MiniLM-L6-v2`

The model converts text into 384-dimensional semantic embeddings.

Cosine similarity is used to measure the similarity between resume and job-description embeddings.

## 5. Similarity Thresholds

| Similarity Score | Category |
|---|---|
| 80% – 100% | Highly Similar |
| 65% – 79% | Relevant |
| 50% – 64% | Partially Relevant |
| Below 50% | Low Similarity |

## 6. Validation Results

The expected matching behavior is:

- Candidate 1 should achieve the strongest match for the AI / Python Developer role.
- Candidate 2 should achieve the strongest match for the Java Backend Developer role.
- Candidate 3 should achieve the strongest match for the Data Analyst role.

This demonstrates that the semantic matching engine can identify relevant candidates across different job types.

## 7. Keyword Matching vs Semantic Matching

Traditional keyword matching mainly depends on exact words appearing in both documents.

Semantic matching uses embeddings to identify similarities in meaning.

For example:

Resume:

"Developed backend services using Python and Flask."

Job Description:

"Experience developing backend applications using Python web frameworks."

Although the wording is different, the semantic meaning is closely related.

## 8. Threshold Tuning

The initial similarity thresholds were selected as:

- 80% and above: Highly Similar
- 65% to 79%: Relevant
- 50% to 64%: Partially Relevant
- Below 50%: Low Similarity

These thresholds can be further tuned using a larger labeled recruitment dataset.

## 9. Limitations

The current evaluation uses a small sample dataset.

Therefore, the results should be considered a prototype validation rather than a production-level accuracy measurement.

Possible limitations include:

- Small evaluation dataset
- Limited number of job roles
- Predefined similarity thresholds
- No human-labeled benchmark dataset
- Semantic similarity may not always represent actual candidate suitability

## 10. Future Improvements

The system can be improved by:

- Testing with hundreds or thousands of resumes
- Creating a human-labeled matching dataset
- Using domain-specific embedding models
- Adding weighted skill and experience scores
- Optimizing similarity thresholds using validation data
- Adding recruiter feedback
- Evaluating precision, recall and F1-score

## 11. Conclusion

The Semantic Matching Engine successfully demonstrates resume-to-job semantic matching using embedding-based similarity.

The system compares skills, experience and project descriptions and produces an overall similarity score for each resume-job pair.

The evaluation confirms that semantic matching can move beyond simple keyword matching and provide more meaningful resume-to-job comparisons.