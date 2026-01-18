import unittest

from textnode import TextNode, TextType
from node_functions import text_to_textnodes


class Test_Text_To_Textnode(unittest.TestCase):

    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, expected)

    def test_text_to_textnode_multiple(self):
        text = "This _is_ **text** _with_ **an** _italic_ word and a `code` `block` and a few ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and links [link](https://boot.dev)[link](https://boot.dev) finish"
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("with", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("an", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("block", TextType.CODE),
            TextNode(" and a few ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and links ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" finish", TextType.TEXT),
        ]
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, expected) 