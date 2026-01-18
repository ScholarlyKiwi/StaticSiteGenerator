import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        children_1 = [ HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        children_2 = [HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        props_1 = {"href": "https://www.google.com",
            "target": "_blank"}
        props_2 = {"href": "https://www.google.com",
            "target": "_blank"}
        node = HTMLNode("h1", "value", children_1, props_1)
        node2 = HTMLNode("h1", "value", children_2, props_2)
        self.assertEqual(node, node2)
    
    def test_neq_tag(self):
        children_1 = [ HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        children_2 = [HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        props_1 = {"href": "https://www.google.com",
            "target": "_blank"}
        props_2 = {"href": "https://www.google.com",
            "target": "_blank"}        
        node = HTMLNode("h1", "value", children_1, props_1)
        node2 = HTMLNode("h2", "value", children_2, props_2)
        self.assertNotEqual(node, node2)

    def test_neq_value(self):
        children_1 = [ HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        children_2 = [HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        props_1 = {"href": "https://www.google.com",
            "target": "_blank"}
        props_2 = {"href": "https://www.google.com",
            "target": "_blank"}        
        node = HTMLNode("h1", "value", children_1, props_1)
        node2 = HTMLNode("h1", "diff_value", children_2, props_2)
        self.assertNotEqual(node, node2)

    def test_neq_children(self):
        children_1 = [ HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        children_2 = [HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2-2 ")]
        props_1 = {"href": "https://www.google.com",
            "target": "_blank"}
        props_2 = {"href": "https://www.google.com",
            "target": "_blank"}        
        node = HTMLNode("h1", "value", children_1, props_1)
        node2 = HTMLNode("h2", "value", children_2, props_2)
        self.assertNotEqual(node, node2)

    def test_neq_props(self):
        children_1 = [ HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2")]
        children_2 = [HTMLNode("p", "paragraph text"),
                        HTMLNode("p", "paragraph text 2 ")]
        props_1 = {"href": "https://www.google.com",
            "target": "_blank"}
        props_2 = {"href": "https://www.boot.dev",
            "target": "_blank"}        
        node = HTMLNode("h1", "value", children_1, props_1)
        node2 = HTMLNode("h2", "value", children_2, props_2)
        self.assertNotEqual(node, node2)   

    def test_eq_none(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        props_1 = {"href": "https://www.google.com",
            "target": "_blank"}
        expected = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode("h1", "none", None, props_1)
        self.assertEqual(node.props_to_html(), expected)