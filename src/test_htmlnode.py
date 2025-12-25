import unittest

from htmlnode import HTMLNode, LeafNode

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




if __name__ == "__main__":
    unittest.main()