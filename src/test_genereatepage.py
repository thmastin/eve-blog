import unittest

from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello World"
        expected_output = "Hello World"

        self.assertEqual(extract_title(md), expected_output)

    def test_extract_title_no_title(self):
        md = "Hello World"
        self.assertRaises(Exception, extract_title, md)

    def test_extract_title_mulitple_lines(self):
        markdown_string = "# My Awesome Title\nThis is the first line of text.\nHere's another line.\nAnd a final line for good measure."
        expected_ooutput = "My Awesome Title"
        self.assertEqual(extract_title(markdown_string), expected_ooutput)

    def test_extract_title_buried_heading(self):
        markdown_string = "Some initial text.\n## A Secondary Heading\nMore text here.\n# The Main Title\n### A Tertiary Heading\nFinal line of text."
        expected_output = "The Main Title"
        self.assertEqual(extract_title(markdown_string), expected_output)

    def test_extract_title_multiple_h1(self):
        markdown_string = "# First Main Title\nSome initial text.\n## A Secondary Heading\nMore text here.\n# Second Main Title\n### A Tertiary Heading\nFinal line of text.\n# Third Main Title"
        expected_output = "First Main Title"
        self.assertEqual(extract_title(markdown_string), expected_output)

    def test_extract_title_headings_no_h1(self):
        markdown_string = "Some initial text.\n## Secondary Heading\nMore text here.\n### Tertiary Heading\nAnother line of text.\n## Another Secondary Heading\nFinal line."
        self.assertRaises(Exception, extract_title, markdown_string)

    def test_extract_title_removes_trailing_whitespace(self):
        markdown_string = "# Hello World          "
        expected_output = "Hello World"
        self.assertEqual(extract_title(markdown_string), expected_output)

if __name__ == "__main__":
    unittest.main()