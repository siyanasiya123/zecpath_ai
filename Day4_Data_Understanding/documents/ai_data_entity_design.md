# AI Data Entity Design Document

## 1. Objective

The objective of this document is to define standardized data entities for processing resumes and job descriptions in an AI-based hiring system.

The entities help convert unstructured hiring information into structured data that can be used for candidate screening, skill matching and job recommendation.

---

# 2. Candidate Profile

The Candidate Profile represents the basic information of a job applicant.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| candidate_id | String | Unique candidate identifier |
| name | String | Candidate name |
| email | String | Candidate email |
| phone | String | Candidate phone number |
| location | String | Candidate location |
| designation | String | Current or previous designation |
| summary | String | Professional summary |

### Example

```json
{
    "candidate_id": "CAND001",
    "name": "Arjun Nair",
    "email": "arjun.nair@example.com",
    "phone": "+91 90000 10001",
    "location": "Kochi, Kerala",
    "designation": "Python Developer",
    "summary": "Python Developer with 2 years of experience."
}
---

# 3. Skill Object

The Skill Object represents a technical or non-technical skill possessed by a candidate or required for a job.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| skill_id | String | Unique skill identifier |
| skill_name | String | Name of the skill |
| category | String | Category of the skill |
| level | String | Skill proficiency level |
| years_of_experience | Number | Years of experience with the skill |

### Example

```json
{
    "skill_id": "SK001",
    "skill_name": "Python",
    "category": "Programming Language",
    "level": "Intermediate",
    "years_of_experience": 2
}
---

# 4. Experience Object

The Experience Object represents a candidate's professional experience, internship experience, or previous employment.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| experience_id | String | Unique experience identifier |
| designation | String | Job designation |
| company | String | Company or organization name |
| start_date | String | Employment start date |
| end_date | String | Employment end date |
| experience_type | String | Full-time, internship, part-time, etc. |
| responsibilities | Array | Responsibilities handled |
| skills_used | Array | Skills used in the role |

### Example

```json
{
    "experience_id": "EXP001",
    "designation": "Python Developer",
    "company": "TechNova Solutions",
    "start_date": "2024-06",
    "end_date": "2026-06",
    "experience_type": "Full-time",
    "responsibilities": [
        "Developed Python applications",
        "Created REST APIs",
        "Worked with databases"
    ],
    "skills_used": [
        "Python",
        "Django",
        "SQL"
    ]
}
---

# 5. Education Object

The Education Object represents the academic qualifications of a candidate.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| education_id | String | Unique education identifier |
| degree | String | Degree or qualification |
| specialization | String | Area of specialization |
| institution | String | Educational institution |
| graduation_year | Number | Year of completion |
| cgpa_or_percentage | String | Academic score |

### Example

```json
{
    "education_id": "EDU001",
    "degree": "MCA",
    "specialization": "Computer Applications",
    "institution": "ABC University",
    "graduation_year": 2027,
    "cgpa_or_percentage": "8.1"
}
# 6. Experience Object

The Experience Object represents the professional experience, internships, and work experience of a candidate.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| experience_id | String | Unique experience identifier |
| company_name | String | Name of the company |
| job_title | String | Job role or position |
| experience_type | String | Internship, full-time, part-time, etc. |
| start_date | String | Start date of the experience |
| end_date | String | End date of the experience |
| responsibilities | String | Main responsibilities and tasks |
| technologies | Array | Technologies and tools used |

### Example

```json
{
    "experience_id": "EXP001",
    "company_name": "XYZ Technologies",
    "job_title": "AI/ML Intern",
    "experience_type": "Internship",
    "start_date": "2026-06-01",
    "end_date": "2026-08-31",
    "responsibilities": "Developed machine learning models and analyzed datasets.",
    "technologies": ["Python", "Pandas", "Scikit-learn", "Machine Learning"]
}
# 7. Project Object

The Project Object represents projects developed or completed by a candidate.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| project_id | String | Unique project identifier |
| project_name | String | Name of the project |
| description | String | Brief description of the project |
| technologies | Array | Technologies and tools used |
| role | String | Candidate's role in the project |
| project_url | String | Link to the project or repository |

### Example

```json
{
    "project_id": "PROJ001",
    "project_name": "AI Resume Analyzer",
    "description": "An AI-based application that analyzes resumes and provides ATS scores and improvement suggestions.",
    "technologies": ["Python", "Streamlit", "Gemini AI", "NLP"],
    "role": "Developer",
    "project_url": "https://github.com/example/ai-resume-analyzer"
}
# 8. Certification Object

The Certification Object represents certifications and professional courses completed by a candidate.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| certification_id | String | Unique certification identifier |
| certification_name | String | Name of the certification |
| issuing_organization | String | Organization that issued the certification |
| issue_date | String | Date the certification was issued |
| expiry_date | String | Expiry date, if applicable |
| credential_id | String | Unique credential or certificate ID |
| credential_url | String | Link to verify the certification |

### Example

```json
{
    "certification_id": "CERT001",
    "certification_name": "Data Science with AI",
    "issuing_organization": "ABC Institute",
    "issue_date": "2026-05-15",
    "expiry_date": null,
    "credential_id": "DSAI12345",
    "credential_url": "https://example.com/verify/DSAI12345"
}
# 9. Candidate Profile Object

The Candidate Profile Object represents the complete profile of a job candidate by combining personal, educational, skill, experience, project, and certification information.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| candidate_id | String | Unique candidate identifier |
| name | String | Full name of the candidate |
| email | String | Candidate email address |
| phone | String | Candidate contact number |
| location | String | Candidate's current location |
| skills | Array | Technical and non-technical skills |
| education | Array | Educational qualifications |
| experience | Array | Work and internship experience |
| projects | Array | Projects completed by the candidate |
| certifications | Array | Certifications obtained by the candidate |

### Example

```json
{
    "candidate_id": "CAN001",
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+91-9876543210",
    "location": "Kerala, India",
    "skills": ["Python", "SQL", "Machine Learning"],
    "education": ["EDU001"],
    "experience": ["EXP001"],
    "projects": ["PROJ001"],
    "certifications": ["CERT001"]
}
# 10. Job Object

The Job Object represents a job vacancy and its requirements.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| job_id | String | Unique job identifier |
| job_title | String | Title of the job |
| company_name | String | Name of the hiring company |
| location | String | Job location |
| job_type | String | Full-time, part-time, internship, etc. |
| description | String | Description of the job |
| required_skills | Array | Skills required for the job |
| preferred_skills | Array | Additional desirable skills |
| experience_required | String | Required experience level |
| education_required | String | Required educational qualification |

### Example

```json
{
    "job_id": "JOB001",
    "job_title": "AI/ML Intern",
    "company_name": "XYZ Technologies",
    "location": "Kochi, Kerala",
    "job_type": "Internship",
    "description": "Work on machine learning and artificial intelligence projects.",
    "required_skills": ["Python", "Machine Learning", "SQL"],
    "preferred_skills": ["Deep Learning", "TensorFlow"],
    "experience_required": "Fresher",
    "education_required": "MCA or equivalent"
}
# 11. Job Requirement Object

The Job Requirement Object represents the specific requirements and qualifications expected from a candidate for a particular job.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| requirement_id | String | Unique requirement identifier |
| job_id | String | Identifier of the related job |
| required_skills | Array | Essential skills required |
| preferred_skills | Array | Additional preferred skills |
| minimum_education | String | Minimum educational qualification |
| experience_level | String | Required experience level |
| certifications | Array | Required or preferred certifications |
| responsibilities | Array | Key responsibilities of the role |

### Example

```json
{
    "requirement_id": "REQ001",
    "job_id": "JOB001",
    "required_skills": ["Python", "Machine Learning", "SQL"],
    "preferred_skills": ["Deep Learning", "TensorFlow"],
    "minimum_education": "MCA or equivalent",
    "experience_level": "Fresher",
    "certifications": ["Machine Learning Certification"],
    "responsibilities": [
        "Develop machine learning models",
        "Analyze datasets",
        "Assist in AI projects"
    ]
}
# 12. Job Application Object

The Job Application Object represents an application submitted by a candidate for a specific job.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| application_id | String | Unique application identifier |
| candidate_id | String | Identifier of the candidate |
| job_id | String | Identifier of the applied job |
| application_date | String | Date of application |
| status | String | Current application status |
| resume_url | String | Link to the candidate's resume |
| cover_letter | String | Candidate's cover letter |
| match_score | Number | Candidate-job matching score |

### Example

```json
{
    "application_id": "APP001",
    "candidate_id": "CAN001",
    "job_id": "JOB001",
    "application_date": "2026-09-24",
    "status": "Applied",
    "resume_url": "https://example.com/resume/CAN001",
    "cover_letter": "I am interested in applying for the AI/ML Intern position.",
    "match_score": 85
}
# 13. Interview Object

The Interview Object represents an interview scheduled or conducted for a candidate applying for a job.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| interview_id | String | Unique interview identifier |
| application_id | String | Identifier of the related job application |
| interview_type | String | Technical, HR, coding, etc. |
| interview_date | String | Scheduled interview date |
| interviewer | String | Name of the interviewer |
| status | String | Scheduled, completed, cancelled, etc. |
| feedback | String | Interviewer's feedback |
| result | String | Interview result |

### Example

```json
{
    "interview_id": "INT001",
    "application_id": "APP001",
    "interview_type": "Technical",
    "interview_date": "2026-10-05",
    "interviewer": "John Smith",
    "status": "Scheduled",
    "feedback": "",
    "result": "Pending"
}
# 14. Assessment Object

The Assessment Object represents a test or evaluation completed by a candidate during the recruitment process.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| assessment_id | String | Unique assessment identifier |
| application_id | String | Identifier of the related job application |
| assessment_type | String | Coding, aptitude, technical, etc. |
| score | Number | Score obtained by the candidate |
| total_score | Number | Maximum possible score |
| assessment_date | String | Date of assessment |
| status | String | Completed, pending, etc. |
| feedback | String | Assessment feedback |

### Example

```json
{
    "assessment_id": "ASM001",
    "application_id": "APP001",
    "assessment_type": "Coding Test",
    "score": 85,
    "total_score": 100,
    "assessment_date": "2026-10-01",
    "status": "Completed",
    "feedback": "Good programming and problem-solving skills."
}
# 15. Candidate Matching Object

The Candidate Matching Object represents the compatibility between a candidate and a job based on skills, education, experience, and other job requirements.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| matching_id | String | Unique matching identifier |
| candidate_id | String | Identifier of the candidate |
| job_id | String | Identifier of the job |
| skill_match_score | Number | Score based on matching skills |
| education_match_score | Number | Score based on educational qualification |
| experience_match_score | Number | Score based on experience |
| overall_match_score | Number | Overall candidate-job matching score |
| matching_status | String | Matched, Partially Matched, or Not Matched |

### Example

```json
{
    "matching_id": "MATCH001",
    "candidate_id": "CAN001",
    "job_id": "JOB001",
    "skill_match_score": 90,
    "education_match_score": 95,
    "experience_match_score": 80,
    "overall_match_score": 88,
    "matching_status": "Matched"
}
# 15. Candidate Matching Object

The Candidate Matching Object represents the compatibility between a candidate and a job based on skills, education, experience, and other job requirements.

### Attributes

| Field | Data Type | Description |
|---|---|---|
| matching_id | String | Unique matching identifier |
| candidate_id | String | Identifier of the candidate |
| job_id | String | Identifier of the job |
| skill_match_score | Number | Score based on matching skills |
| education_match_score | Number | Score based on educational qualification |
| experience_match_score | Number | Score based on experience |
| overall_match_score | Number | Overall candidate-job matching score |
| matching_status | String | Matching result status |

### Example

```json
{
    "matching_id": "MATCH001",
    "candidate_id": "CAN001",
    "job_id": "JOB001",
    "skill_match_score": 90,
    "education_match_score": 95,
    "experience_match_score": 80,
    "overall_match_score": 88,
    "matching_status": "Matched"
}
# 16. Object Relationships

The Object Relationships define how the different objects in the recruitment system are connected to each other.

### Relationships

| Relationship | Description |
|---|---|
| Candidate → Skills | A candidate can have multiple skills |
| Candidate → Education | A candidate can have multiple educational qualifications |
| Candidate → Experience | A candidate can have multiple work experiences |
| Candidate → Projects | A candidate can have multiple projects |
| Candidate → Certifications | A candidate can have multiple certifications |
| Candidate → Job Application | A candidate can submit multiple job applications |
| Job → Job Requirements | A job can have multiple requirements |
| Job → Job Applications | A job can receive multiple applications |
| Job Application → Interview | An application can have one or more interviews |
| Job Application → Assessment | An application can have one or more assessments |
| Candidate → Candidate Matching | A candidate can be matched with multiple jobs |
| Job → Candidate Matching | A job can be matched with multiple candidates |

### Relationship Structure

```text
Candidate
    |
    ├── Skills
    ├── Education
    ├── Experience
    ├── Projects
    ├── Certifications
    └── Job Applications
              |
              ├── Interview
              └── Assessment

Job
    |
    ├── Job Requirements
    ├── Job Applications
    └── Candidate Matching
    # 17. Complete Data Model Example

The following example demonstrates how the main objects are connected in the recruitment system.

### Complete Example

```json
{
    "candidate": {
        "candidate_id": "CAN001",
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "+91-9876543210",
        "location": "Kerala, India"
    },

    "skills": [
        {
            "skill_id": "SKL001",
            "skill_name": "Python",
            "category": "Programming",
            "level": "Advanced"
        },
        {
            "skill_id": "SKL002",
            "skill_name": "Machine Learning",
            "category": "Artificial Intelligence",
            "level": "Intermediate"
        }
    ],

    "education": [
        {
            "education_id": "EDU001",
            "degree": "MCA",
            "specialization": "Computer Applications",
            "institution": "ABC University",
            "graduation_year": 2027,
            "cgpa_or_percentage": "8.1"
        }
    ],

    "experience": [
        {
            "experience_id": "EXP001",
            "company_name": "XYZ Technologies",
            "job_title": "AI/ML Intern",
            "experience_type": "Internship",
            "technologies": [
                "Python",
                "Pandas",
                "Scikit-learn"
            ]
        }
    ],

    "projects": [
        {
            "project_id": "PROJ001",
            "project_name": "AI Resume Analyzer",
            "technologies": [
                "Python",
                "Streamlit",
                "Gemini AI",
                "NLP"
            ],
            "role": "Developer"
        }
    ],

    "certifications": [
        {
            "certification_id": "CERT001",
            "certification_name": "Data Science with AI",
            "issuing_organization": "ABC Institute"
        }
    ],

    "job": {
        "job_id": "JOB001",
        "job_title": "AI/ML Intern",
        "company_name": "XYZ Technologies",
        "location": "Kochi, Kerala",
        "job_type": "Internship",
        "required_skills": [
            "Python",
            "Machine Learning",
            "SQL"
        ]
    },

    "job_application": {
        "application_id": "APP001",
        "candidate_id": "CAN001",
        "job_id": "JOB001",
        "status": "Applied",
        "match_score": 85
    },

    "interview": {
        "interview_id": "INT001",
        "application_id": "APP001",
        "interview_type": "Technical",
        "status": "Scheduled",
        "result": "Pending"
    },

    "assessment": {
        "assessment_id": "ASM001",
        "application_id": "APP001",
        "assessment_type": "Coding Test",
        "score": 85,
        "total_score": 100,
        "status": "Completed"
    },

    "candidate_matching": {
        "matching_id": "MATCH001",
        "candidate_id": "CAN001",
        "job_id": "JOB001",
        "skill_match_score": 90,
        "education_match_score": 95,
        "experience_match_score": 80,
        "overall_match_score": 88,
        "matching_status": "Matched"
    }
}
# 18. Final Schema / Summary

The recruitment system data model provides a structured representation of candidates, jobs, applications, assessments, interviews, and candidate-job matching.

### Main Objects

| No. | Object                    | Purpose                                   |
| --- | ------------------------- | ----------------------------------------- |
| 1   | Candidate Object          | Stores basic candidate information        |
| 2   | Skill Object              | Stores candidate skills and proficiency   |
| 3   | Experience Object         | Stores work and internship experience     |
| 4   | Education Object          | Stores academic qualifications            |
| 5   | Project Object            | Stores candidate projects                 |
| 6   | Certification Object      | Stores certifications and courses         |
| 7   | Candidate Profile Object  | Combines candidate profile information    |
| 8   | Job Object                | Stores job vacancy information            |
| 9   | Job Requirement Object    | Stores job requirements                   |
| 10  | Job Application Object    | Stores candidate job applications         |
| 11  | Interview Object          | Stores interview information              |
| 12  | Assessment Object         | Stores candidate assessment details       |
| 13  | Candidate Matching Object | Stores candidate-job matching information |

### Overall Data Flow

```text
Candidate
    ↓
Profile
    ↓
Skills + Education + Experience + Projects + Certifications
    ↓
Job Matching
    ↓
Job Application
    ↓
Assessment
    ↓
Interview
    ↓
Selection Process
```

### Conclusion

The proposed data model organizes candidate and job information into separate but connected objects. This structure makes the recruitment system easier to manage, search, analyze, and extend. It also supports automated candidate-job matching, assessment tracking, interview management, and future AI-based recruitment features.
