import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_div(self):
        node = HTMLNode("div", "hello", None, {"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')

    def test_link(self):
        node = HTMLNode("a", None, None, {"href": "google.com"})
        self.assertEqual(node.props_to_html(),' href="google.com"')

    def test_with_target(self):
        node = HTMLNode("a", None, None, {"href": "google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="google.com" target="_blank"')
    
    def test_no_prop(self):
        node = HTMLNode("p", "this is a paragraph text without prop")
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_link(self):
        node = LeafNode("a", "google.com", {"href": "google.com"})
        self.assertEqual(node.to_html(), '<a href="google.com">google.com</a>')

    def test_leaf_no_tag(self):
        node = LeafNode(None, "This text has no tag.")
        self.assertEqual(node.to_html(), "This text has no tag.")

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
    def test_to_html_no_tag(self):
        child_node = LeafNode("b", "No tag test.")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()