import unittest

from node_functions import *


class Test_split_nodes_link(unittest.TestCase):

    def test_split_nodes_link_simple(self):
        old_nodes = [(TextNode("This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT))]
        new_nodes = split_nodes_link(old_nodes)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png")
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_link_links_only(self):
        old_nodes = [(TextNode("[image](https://i.imgur.com/zjjcJKZ.png)[second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT))]
        new_nodes = split_nodes_link(old_nodes)
        expected = [
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png")
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_link_repeat(self):
        old_nodes = [(TextNode("This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and repeat [image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT))]
        new_nodes = split_nodes_link(old_nodes)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and repeat ", TextType.TEXT),
            TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")
        ]
        self.assertEqual(new_nodes, expected)