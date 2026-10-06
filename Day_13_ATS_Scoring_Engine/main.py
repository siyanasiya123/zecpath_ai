# Day 13 - ATS Scoring System
# Main application

import json
from pathlib import Path

from scoring_engine import generate_candidate_score
from explainable_output import create_explainable_output


BASE_DIR = Path(__file__).resolve().parent

CANDIDATE_FILE = (
    BASE_DIR / "data" / "candidate_profile.json"
)

JOB_FILE = (
    BASE_DIR / "data" / "job_requirements.json"
)

OUTPUT_FILE = (
    BASE_DIR / "output" / "candidate_score.json"
)


def load_json(file_path):
    """Load JSON data from a file."""

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_json(data, file_path):
    """Save data as formatted JSON."""

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def main():

    candidate = load_json(
        CANDIDATE_FILE
    )

    job = load_json(
        JOB_FILE
    )

    score_result = generate_candidate_score(
        candidate,
        job
    )

    explainable_result = create_explainable_output(
        score_result,
        job.get("role", "Unknown")
    )

    final_result = {
        "candidate_id": candidate.get(
            "candidate_id",
            "Unknown"
        ),

        "candidate_name": candidate.get(
            "candidate_name",
            "Unknown"
        ),

        "job_id": job.get(
            "job_id",
            "Unknown"
        ),

        "target_role": job.get(
            "role",
            "Unknown"
        ),

        "score_result": explainable_result
    }

    save_json(
        final_result,
        OUTPUT_FILE
    )

    print("\n======================================")
    print("DAY 13 ATS SCORING ENGINE")
    print("======================================")

    print(
        "\nCandidate:",
        candidate.get(
            "candidate_name",
            "Unknown"
        )
    )

    print(
        "Target Role:",
        job.get(
            "role",
            "Unknown"
        )
    )

    print("\nScore Breakdown:")

    breakdown = explainable_result[
        "score_breakdown"
    ]

    for parameter, score in breakdown.items():

        print(
            f"{parameter}: {score}%"
        )

    print(
        "\nFinal ATS Score:",
        explainable_result["final_score"],
        "/ 100"
    )

    print(
        "Category:",
        explainable_result["category"]
    )

    print("\nExplanation:")

    for explanation in explainable_result[
        "explanation"
    ]:

        print(
            "-",
            explanation
        )

    print("\nResults saved to:")

    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()