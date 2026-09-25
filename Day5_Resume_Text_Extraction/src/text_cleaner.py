import re


def clean_text(text):
    """
    Remove unwanted symbols, spaces and formatting noise.
    """

    if not text:
        return ""

    # Replace multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Normalize bullet symbols
    text = text.replace("•", "-")
    text = text.replace("▪", "-")
    text = text.replace("●", "-")
    text = text.replace("◦", "-")

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove unwanted control characters
    text = re.sub(
        r"[\x00-\x08\x0B\x0C\x0E-\x1F]",
        "",
        text
    )

    return text.strip()