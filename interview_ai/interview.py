class InterviewAI:

    def create_interview(self, candidate_name, job_role):
        """
        Base interview module.
        """

        return {
            "candidate": candidate_name,
            "job_role": job_role,
            "status": "NOT_STARTED"
        }
