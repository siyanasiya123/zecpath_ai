class ScreeningAI:

    def screen_candidate(self, candidate_data):
        """
        Base candidate screening module.
        """

        return {
            "candidate": candidate_data,
            "status": "PENDING"
        }
