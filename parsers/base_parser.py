class BaseParser:

    def parse(self, file_path):
        """
        Base document parser.
        Actual document parsing can be implemented later.
        """

        return {
            "file_path": file_path,
            "text": ""
        }