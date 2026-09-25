import json
from pathlib import Path

from extractor import extract_resume_data


BASE_DIR = Path(__file__).resolve().parent.parent

STRUCTURED_DIR = BASE_DIR / "data" / "structured"
FINAL_DIR = BASE_DIR / "data" / "final"

FINAL_DIR.mkdir(parents=True, exist_ok=True)


def fix_encoding(text):
    """Fix common UTF-8 mojibake encoding problems."""

    if not text:
        return ""

    replacements = {
        "\u00e2\u20ac\u201c": "-",   # â€“
        "\u00e2\u20ac\u201d": "-",   # â€”
        "\u00e2\u20ac\u02dc": "'",   # â€˜
        "\u00e2\u20ac\u2122": "'",   # â€™
        "\u00e2\u20ac\u0153": '"',   # â€œ
        "\u00e2\u20ac\u009d": '"',   # â€
        "\u00e2\u20ac\u00a2": "*",   # â€¢
        "\u00c2": ""                 # Â
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def main():

    json_files = list(STRUCTURED_DIR.glob("*.json"))

    print(f"Found {len(json_files)} JSON file(s).")

    for json_file in json_files:

        print(f"\nProcessing: {json_file.name}")

        # utf-8-sig supports both normal UTF-8 and UTF-8 with BOM
        with open(
            json_file,
            "r",
            encoding="utf-8-sig"
        ) as file:
            data = json.load(file)

        raw_text = data.get("raw_text", "")

        # Fix encoding before extraction
        raw_text = fix_encoding(raw_text)

        # Extract structured information
        structured_data = extract_resume_data(raw_text)

        # Fix encoding in all extracted fields
        for key, value in structured_data.items():

            if isinstance(value, str):
                structured_data[key] = fix_encoding(value)

            elif isinstance(value, list):
                structured_data[key] = [
                    fix_encoding(item) if isinstance(item, str) else item
                    for item in value
                ]

        output_file = FINAL_DIR / json_file.name

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                structured_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()