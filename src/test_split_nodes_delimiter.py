import unittest

from textnode import TextNode, TextType
from node_functions import split_nodes_delimiter


class Test_Text_To_HTML(unittest.TestCase):

    def test_simple_splt_bold(self):
        node = TextNode("This is a **text** node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" node", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_start_splt(self):
        node = TextNode("**This is a **text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.BOLD),
            TextNode("text node", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_end_splt(self):
        node = TextNode("This is a **text node**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("text node", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected)

    def test_nest_inline(self):
        node = TextNode("This is a **te__xt no__de**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("te__xt no__de", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        node = TextNode("Text node _italic_ test")
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("Text node ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" test", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        node = TextNode("Text node `code` test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text node ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" test", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_nodes(self):
        nodes = [TextNode("Text node `code` test", TextType.TEXT), TextNode("Second `code` test", TextType.TEXT), TextNode("`Third code` test", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("Text node ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" test", TextType.TEXT),
            TextNode("Second ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" test", TextType.TEXT),
            TextNode("Third code", TextType.CODE),
            TextNode(" test", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)