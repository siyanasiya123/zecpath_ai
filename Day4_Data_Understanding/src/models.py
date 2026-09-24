from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Candidate:
    candidate_id: str
    name: str
    email: str
    phone: str
    location: str


@dataclass
class Skill:
    skill_id: str
    skill_name: str
    category: str
    level: str


@dataclass
class Experience:
    experience_id: str
    company_name: str
    job_title: str
    experience_type: str
    start_date: str
    end_date: str
    responsibilities: str
    technologies: List[str] = field(default_factory=list)


@dataclass
class Education:
    education_id: str
    degree: str
    specialization: str
    institution: str
    graduation_year: int
    cgpa_or_percentage: str


@dataclass
class Project:
    project_id: str
    project_name: str
    description: str
    technologies: List[str] = field(default_factory=list)
    role: str = ""
    project_url: str = ""


@dataclass
class Certification:
    certification_id: str
    certification_name: str
    issuing_organization: str
    issue_date: str
    expiry_date: Optional[str] = None
    credential_id: str = ""
    credential_url: str = ""


@dataclass
class Job:
    job_id: str
    job_title: str
    company_name: str
    location: str
    job_type: str
    description: str
    required_skills: List[str] = field(default_factory=list)
    preferred_skills: List[str] = field(default_factory=list)
    experience_required: str = ""
    education_required: str = ""


@dataclass
class JobApplication:
    application_id: str
    candidate_id: str
    job_id: str
    application_date: str
    status: str
    resume_url: str = ""
    cover_letter: str = ""
    match_score: float = 0.0


@dataclass
class Interview:
    interview_id: str
    application_id: str
    interview_type: str
    interview_date: str
    interviewer: str
    status: str
    feedback: str = ""
    result: str = "Pending"


@dataclass
class Assessment:
    assessment_id: str
    application_id: str
    assessment_type: str
    score: float
    total_score: float
    assessment_date: str
    status: str
    feedback: str = ""


@dataclass
class CandidateMatching:
    matching_id: str
    candidate_id: str
    job_id: str
    skill_match_score: float
    education_match_score: float
    experience_match_score: float
    overall_match_score: float
    matching_status: str