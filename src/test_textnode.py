import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("Some text", TextType.TEXT)
        node2 = TextNode("Some text 2", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("Some text", TextType.ITALIC, "https://www.google.com")
        node2 = TextNode("Some text", TextType.ITALIC, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Some text", TextType.TEXT, "https://www.google.com")
        self.assertEqual("TextNode(Some text, text, https://www.google.com)", repr(node))

if __name__ == "__main__":
    unittest.main()