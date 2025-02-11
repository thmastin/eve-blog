import unittest

from htmlnode import HTMLNode


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
        


if __name__ == "__main__":
    unittest.main()