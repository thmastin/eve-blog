import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    #LeafNode Tests
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
    
    # ParentNode Tests
    def test_simple_parent_with_leaf_children(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Paragraph 1"), LeafNode("p", "Paragraph 2")]
        )
        output = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"
        self.assertEqual(node.to_html(), output)

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "Paragraph 1"),
                ParentNode("section", [LeafNode("p", "Nested Paragraph")])
            ]
        )
        output = "<div><p>Paragraph 1</p><section><p>Nested Paragraph</p></section></div>"
        self.assertEqual(node.to_html(), output)

    def test_parent_with_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Paragraph 1")]).to_html()

    def test_parent_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_parent_with_empty_children(self):
        node = ParentNode("div", [])
        output = "<div></div>"
        self.assertEqual(node.to_html(), output)

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Paragraph 1")],
            props={"class": "container", "id": "main"}
        )
        output = '<div class="container" id="main"><p>Paragraph 1</p></div>'
        self.assertEqual(node.to_html(), output)

    def test_deeply_nested_children(self):
        # Deeply nested ParentNodes with LeafNodes inside
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "article",
                            [LeafNode("p", "Deepest Layer of Text")]
                        )
                    ]
                )
            ]
        )
        output = "<div><section><article><p>Deepest Layer of Text</p></article></section></div>"
        self.assertEqual(node.to_html(), output)

    def test_mixed_nested_children(self):
        # A mix of LeafNodes and ParentNodes at various levels
        node = ParentNode(
            "html",
            [
                ParentNode(
                    "body",
                    [
                        LeafNode("h1", "Header Text"),
                        ParentNode(
                            "div",
                            [
                                LeafNode("p", "Paragraph 1"),
                                LeafNode("p", "Paragraph 2"),
                            ]
                        ),
                        LeafNode("footer", "Footer Text")
                    ]
                )
            ]
        )
        output = "<html><body><h1>Header Text</h1><div><p>Paragraph 1</p><p>Paragraph 2</p></div><footer>Footer Text</footer></body></html>"
        self.assertEqual(node.to_html(), output)

    def test_property_propagation_in_nested_parents(self):
        # Adding properties and verifying they're propagated correctly
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [LeafNode("p", "Inner Text")],
                    props={"class": "nested-section"}
                )
            ],
            props={"class": "outer-div", "id": "container"}
        )
        output = '<div class="outer-div" id="container"><section class="nested-section"><p>Inner Text</p></section></div>'
        self.assertEqual(node.to_html(), output)

    def test_nested_with_empty_children(self):
        # Empty children in a ParentNode
        node = ParentNode(
            "main",
            [
                ParentNode("header", []),
                ParentNode("section", []),
            ]
        )
        output = "<main><header></header><section></section></main>"
        self.assertEqual(node.to_html(), output)
    


if __name__ == "__main__":
    unittest.main()