import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    
    def test_props(self):
        properties = {
            "href": "https://www.google.com",
            "target": "_blank" 
        }
        node = HTMLNode(props=properties)
        output = ' href="https://www.google.com" target="_blank"' 
        self.assertEqual(node.props_to_html(), output)

    def test_one_prop(self):
        properties = {"href": "https://www.google.com"} 
        node = HTMLNode(props=properties)
        output = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), output)   

    def test_three_props(self):
        properties = {
            "href": "https://www.google.com",
            "target": "_blank" ,
            "lang": "en"
        }
        node = HTMLNode(props=properties)
        output = ' href="https://www.google.com" target="_blank" lang="en"'
        self.assertEqual(node.props_to_html(), output) 

    def test_empty_props(self):
        node = HTMLNode()
        output = ""
        self.assertEqual(node.props_to_html(), output)
    
    def test_empty_dict_props(self):
        node = HTMLNode(props={})
        output = ""
        self.assertEqual(node.props_to_html(), output)

    def test_leaf_no_value(self):
        node = LeafNode(tag=None, value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_no_tag(self):
        node = LeafNode(tag=None, value="This is plain text")
        output = "This is plain text"
        self.assertEqual(node.to_html(), output)

    def test_leaf_tag_and_value(self):
        node = LeafNode("p", "This is a paragraph of text.")
        output = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), output)

    def test_leaf_tag_value_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        output = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), output)
    
    def test_leaf_empty_string_value(self):
        node = LeafNode(tag=None, value="")
        output = ""
        self.assertEqual(node.to_html(), output)

    def test_lef_empty_string_tag(self):
        node = LeafNode("", "This is invalid HTML")
        output = '<>This is invalid HTML</>'
        self.assertEqual(node.to_html(), output)


if __name__ == "__main__":
    unittest.main()