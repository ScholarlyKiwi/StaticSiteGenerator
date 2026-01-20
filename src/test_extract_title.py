import unittest

from page_functions import extract_title
from textnode import TextNode, TextType

class Test_Extract_Title(unittest.TestCase):

    def test_extract_title_heading_start(self):
        markdown = """# title found
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        expected = "title found"
        heading = extract_title(markdown).strip()
        self.assertEqual(heading, expected)

    def test_extract_title_heading_start_cr(self):
        markdown = """
# title found
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        expected = "title found"
        heading = extract_title(markdown).strip()
        self.assertEqual(heading, expected)

    def test_extract_title_no_heading(self):
        markdown = """title not found
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        with self.assertRaises(Exception) as cm:
            title = extract_title(markdown)
        self.assertEqual(str(cm.exception), "Markdown has no header for title.")
        
    def test_extract_title_heading_later(self):
        markdown = """

This is **bolded** paragraph

# title found

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        expected = "title found"
        heading = extract_title(markdown).strip()
        self.assertEqual(heading, expected)