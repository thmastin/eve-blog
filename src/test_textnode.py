import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node that is not equal", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_text_node_to_html_node(self):
        # Test regular text node
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"

        # Test invalid type
        invalid_node = TextNode("test", "not_a_valid_type")  # or could use a different value
        try:
            text_node_to_html_node(invalid_node)
            assert False, "Expected an exception for invalid type"
        except Exception as e:
            assert "Invalid text type" in str(e)

        #test bold text node
        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "b"
        assert html_node.value == "Hello, world!"

        #test italic text node
        text_node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "i"
        assert html_node.value == "Hello, world!"

        #test code text node
        text_node = TextNode("Hello, world!", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "code"
        assert html_node.value == "Hello, world!"

        #test link text node
        text_node = TextNode("Hello, world!", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "a"
        assert html_node.value == "Hello, world!"
        assert html_node.props == {"href": "https://google.com"} 

        #test image text node
        text_node = TextNode("hello, world", TextType.IMAGE, "https://google.com")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props ==  {
                "src": "https://google.com",
                "alt": "hello, world"
            }

if __name__ == "__main__":
    unittest.main()