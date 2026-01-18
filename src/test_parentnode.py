import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_h1_p_a(self):
        props = {"href": "https://www.google.com"}        
        node = ParentNode("h1", [LeafNode("p", "Click here to go to:"), LeafNode("a", "google", props)])
        self.assertEqual(node.to_html(), '<h1><p>Click here to go to:</p><a href="https://www.google.com">google</a></h1>')

    def test_parent_no_children(self):
        node = ParentNode("div", None, None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), 'ParentNode has no children.')

    def test_parent_no_tag(self):
        node = ParentNode(None, LeafNode("p", "value"), None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), 'ParentNode has no tag.')

    def test_parent_eq(self):
        props_1 = {"href": "https://www.google.com"}
        props_2 = {"href": "https://www.google.com"}
        node_1 = ParentNode("h1", [LeafNode("p", "Click here to go to:"), LeafNode("a", "google", props_1)])
        node_2 = ParentNode("h1", [LeafNode("p", "Click here to go to:"), LeafNode("a", "google", props_2)])
        self.assertEqual(node_1, node_2)

    def test_parent_neq_props(self):
        props_1 = {"href": "https://www.google.com"}
        props_2 = {"href": "https://www.boot.dev"}
        node_1 = ParentNode("h1", [LeafNode("p", "Click here to go to:"), LeafNode("a", "google", props_1)])
        node_2 = ParentNode("h1", [LeafNode("p", "Click here to go to:"), LeafNode("a", "google", props_2)])
        self.assertNotEqual(node_1, node_2)     