from typing import List
from models import (
    Candidate,
    Skill,
    Experience,
    Education,
    Project,
    Certification,
    Job,
    JobApplication,
    Interview,
    Assessment,
    CandidateMatching
)


class CandidateProfile:
    def __init__(
        self,
        candidate: Candidate,
        skills: List[Skill] = None,
        experiences: List[Experience] = None,
        education: List[Education] = None,
        projects: List[Project] = None,
        certifications: List[Certification] = None
    ):
        self.candidate = candidate
        self.skills = skills or []
        self.experiences = experiences or []
        self.education = education or []
        self.projects = projects or []
        self.certifications = certifications or []

    def __repr__(self):
        return (
            f"CandidateProfile("
            f"candidate={self.candidate.name}, "
            f"skills={len(self.skills)}, "
            f"education={len(self.education)}, "
            f"projects={len(self.projects)}, "
            f"certifications={len(self.certifications)})"
        )


class JobProfile:
    def __init__(
        self,
        job: Job,
        applications: List[JobApplication] = None
    ):
        self.job = job
        self.applications = applications or []

    def __repr__(self):
        return (
            f"JobProfile("
            f"job={self.job.job_title}, "
            f"company={self.job.company_name}, "
            f"applications={len(self.applications)})"
        )


class ApplicationDetails:
    def __init__(
        self,
        application: JobApplication,
        interviews: List[Interview] = None,
        assessments: List[Assessment] = None,
        matching: CandidateMatching = None
    ):
        self.application = application
        self.interviews = interviews or []
        self.assessments = assessments or []
        self.matching = matching

    def __repr__(self):
        return (
            f"ApplicationDetails("
            f"application={self.application.application_id}, "
            f"interviews={len(self.interviews)}, "
            f"assessments={len(self.assessments)}, "
            f"match_score={self.application.match_score})"
        )