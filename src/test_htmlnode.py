import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_working(self):
        node = HTMLNode(
            "a",
            "click",
            None,
            {"href": "https://www.google.com", "target": "_blank"},       
        )

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"',)
    
    def test_arguments(self):
        node = HTMLNode(
            "a",
            "clicky clicky",
        )
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "clicky clicky")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("a", "some random text", None, {"attribute": "value"},)
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=a, value=some random text, children=None, props={'attribute': 'value'})",
        )

    # LeafNode tests

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_tags(self):
        node = LeafNode(None, "some random text")
        self.assertEqual(node.to_html(), "some random text")
    
    def test_leaf_repr(self):
        node = LeafNode("a", "some random text", {"attribute": "value"},)
        self.assertEqual(
            node.__repr__(),
            "LeafNode(tag=a, value=some random text, props={'attribute': 'value'})",
        )

    # ParentNode tests

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
    
    def test_to_html_several_children(self):
        node = ParentNode(
            "p",
            [
            LeafNode("i", "italic text"),
            LeafNode(None, "normal text"),
            LeafNode("b", "bold text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><i>italic text</i>normal text<b>bold text</b></p>")

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",)


    def test_parent_no_children(self): # Testing exception raising
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        expected_message = "Invalid HTML: ParentNode is missing a children value"
        self.assertEqual(str(cm.exception), expected_message)

    def test_parent_no_value(self): # Testing exception raising
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        expected_message = "Invalid HTML: ParentNode has no tag value assigned"
        self.assertEqual(str(cm.exception), expected_message)
    
    def test_parent_repr(self):
        node = ParentNode("h2", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),],)
        self.assertEqual(
            node.__repr__(),
            "ParentNode(tag=h2, children=[LeafNode(tag=b, value=Bold text, props=None), LeafNode(tag=None, value=Normal text, props=None)], props=None)"
        )
    
    
if __name__ == "__main__":
    unittest.main()