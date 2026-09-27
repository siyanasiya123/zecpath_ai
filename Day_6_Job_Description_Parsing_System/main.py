import json
from pathlib import Path

from jd_parser import parse_job_description

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "data" / "sample_jds.txt"
OUTPUT_FILE = BASE_DIR / "output" / "jd_output_samples.json"


def main():
    try:
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

        if not INPUT_FILE.exists():
            print("Input file not found:", INPUT_FILE)
            return

        job_description = INPUT_FILE.read_text(
            encoding="utf-8"
        )

        parsed_data = parse_job_description(job_description)

        with OUTPUT_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                parsed_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Job description parsed successfully!")
        print("\nStructured Output:")
        print(json.dumps(parsed_data, indent=4, ensure_ascii=False))
        print("\nOutput saved to:", OUTPUT_FILE)

    except ValueError as error:
        print("Input error:", error)

    except OSError as error:
        print("File error:", error)


if __name__ == "__main__":
    main()