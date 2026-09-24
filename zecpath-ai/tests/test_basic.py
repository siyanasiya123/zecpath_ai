from parsers.base_parser import BaseParser


def test_parser():

    parser = BaseParser()

    result = parser.parse("sample_resume.pdf")

    assert result["file_path"] == "sample_resume.pdf"
    assert result["text"] == ""
