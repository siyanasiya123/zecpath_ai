from docx import Document


def extract_text_from_docx(file_path):
    """
    Extract text from a DOCX resume.
    """

    document = Document(file_path)

    extracted_text = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if text:
            extracted_text.append(text)

    return "\n".join(extracted_text)