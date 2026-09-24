import json

FILE_PATH = "extracted_data/raw_resume_data.json"


def main():

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            resumes = json.load(file)

        print("=" * 70)
        print("EXTRACTED RESUME DATA")
        print("=" * 70)

        print(f"\nTotal resumes: {len(resumes)}\n")

        for i, resume in enumerate(resumes, start=1):

            print("-" * 70)
            print(f"RESUME {i}")
            print("-" * 70)

            print(f"File: {resume['resume_file']}")
            print("\nExtracted Text:")
            print(resume["raw_text"])

        print("\n" + "=" * 70)
        print("DATA DISPLAY COMPLETED")
        print("=" * 70)

    except FileNotFoundError:
        print("ERROR: raw_resume_data.json was not found.")
        print("Run the resume extraction program first.")

    except json.JSONDecodeError:
        print("ERROR: JSON file is not valid.")

    except Exception as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()