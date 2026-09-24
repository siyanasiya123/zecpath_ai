import os
import json
from PyPDF2 import PdfReader


RESUME_FOLDER = "resumes"
OUTPUT_FOLDER = "extracted_data"


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_all_resumes():

    # Create output folder if it doesn't exist
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    all_resumes = []

    # Check whether resumes folder exists
    if not os.path.exists(RESUME_FOLDER):
        print("ERROR: resumes folder not found.")
        return

    # Read all PDF files
    for filename in sorted(os.listdir(RESUME_FOLDER)):

        if filename.lower().endswith(".pdf"):

            pdf_path = os.path.join(
                RESUME_FOLDER,
                filename
            )

            print(f"Processing: {filename}")

            try:
                text = extract_text_from_pdf(pdf_path)

                resume = {
                    "resume_file": filename,
                    "raw_text": text
                }

                all_resumes.append(resume)

            except Exception as error:
                print(f"Error processing {filename}: {error}")

    # Save extracted data
    output_path = os.path.join(
        OUTPUT_FOLDER,
        "raw_resume_data.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_resumes,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\n" + "=" * 50)
    print("RESUME EXTRACTION COMPLETED")
    print("=" * 50)

    print(f"Total resumes processed: {len(all_resumes)}")
    print(f"Output file: {output_path}")


if __name__ == "__main__":
    extract_all_resumes()