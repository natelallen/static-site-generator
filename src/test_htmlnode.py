import unittest

from htmlnode import HTMLNode

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
        node = HTMLNode(
            "a",
            "some random text",
            None,
            {"attribute": "value"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=a, value=some random text, children=None, props={'attribute': 'value'})",
        )

if __name__ == "__main__":
    unittest.main()