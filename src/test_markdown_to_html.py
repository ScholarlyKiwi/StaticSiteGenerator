import unittest

from node_functions import *


class Test_Markdown_to_HTML(unittest.TestCase):


    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """Below is an unordered list:

- List Item 1
- List Item 2
- List Item 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Below is an unordered list:</p><ul><li>List Item 1</li><li>List Item 2</li><li>List Item 3</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """Below is an ordered list:

1. List Item 1
2. List Item 2
3. List Item 3"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Below is an ordered list:</p><ol><li>List Item 1</li><li>List Item 2</li><li>List Item 3</li></ol></div>"
        )

    def test_block_quote(self):
        md = """> This is the first line of a quote
> This is the second line of a quote, but it may not be
> This is the end of the quote"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is the first line of a quote This is the second line of a quote, but it may not be This is the end of the quote</p></blockquote></div>"
        )