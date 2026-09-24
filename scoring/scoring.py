class ScoringEngine:

    def calculate_score(self, ats_score, interview_score=0):
        """
        Basic score calculation.
        """

        overall_score = (ats_score + interview_score) / 2

        return round(overall_score, 2)
