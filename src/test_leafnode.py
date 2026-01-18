import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_neq(self):
        node = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<p>Hello, worldd!</p>")

    def test_props_to_html(self):
        props_1 = {"href": "https://www.google.com",
            "target": "_blank"}
        expected = ' href="https://www.google.com" target="_blank"'
        node = LeafNode("h1", "none", props_1)
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_to_html_a(self):
        props= {"href": "https://www.google.com"}
        node = LeafNode("a", "Hello, world!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')