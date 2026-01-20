import unittest

from node_functions import *


class TestLeafNode(unittest.TestCase):

    def test_extract_markdown_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        results = extract_markdown_links(text)
        self.assertEqual(results, expected)

    def test_extract_markdown_links_start(self):
        text = "[rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        results = extract_markdown_links(text)
        self.assertEqual(results, expected)

    def test_extract_markdown_links_together(self):
        text = "[rick roll](https://i.imgur.com/aKaOqIh.gif)[obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        results = extract_markdown_links(text)
        self.assertEqual(results, expected)

    def test_extract_markdown_links_no_alt(self):
        text = "[](https://i.imgur.com/aKaOqIh.gif) [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        results = extract_markdown_links(text)
        self.assertEqual(results, expected)

    def test_extract_markdown_links_glorfindel(self):
        text = """# Why Glorfindel is More Impressive than Legolas

[< Back Home](/)

![Glorfindel image](/images/glorfindel.png)"""
        expected = [("< Back Home", "/")]
        results = extract_markdown_links(text)
        self.assertEqual(results, expected)