import unittest

from splitnode import split_nodes_delimiter, extract_markdown_images, extract_markdown_links,split_nodes_image, split_nodes_links
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_no_delimiters(self):
        # Input: A single TextNode with no delimiters
        node = TextNode("There is no delimiter here", TextType.TEXT)
        # Expected: The same node returned as a single-item list
        expected_output = [node]
        
        # Call the split_nodes_delimiter function
        actual_output = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        # Assert equality
        self.assertEqual(actual_output, expected_output)
    
    def test_no_closing_delimiter(self):
        # Input: A single TextNode with an opening bold delimiter but no closing
        node = TextNode("This is normal. **This is bold. This is normal", TextType.TEXT)

        # Expect the function to raise an exception
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)

        # Check if the exception message matches
        self.assertEqual(
            str(context.exception), "Invalid Markdown Syntax: Must have closing **"
        ) 
    
    def test_one_delimiter(self):
        # Input: A single TextNode with properly paired bold delimiters
        node = TextNode("This is normal. **This is bold.** This is normal", TextType.TEXT)
        
        # Expected Output: Split into three nodes
        expected_output = [
            TextNode("This is normal. ", TextType.TEXT),
            TextNode("This is bold.", TextType.BOLD),
            TextNode(" This is normal", TextType.TEXT),
        ]
        
        # Call the split_nodes_delimiter function
        actual_output = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        # Assert equality
        self.assertEqual(actual_output, expected_output)

    def test_multiple_delimiters(self):
        # Input a single TExtNode with two sets of properly paired bold delimiters
        node = TextNode("This is normal. **This is bold.** This is normal **This is bold.**", TextType.TEXT)

        # Expected Output: Split into four nodes
        expected_output = [
            TextNode("This is normal. ", TextType.TEXT),
            TextNode("This is bold.", TextType.BOLD),
            TextNode(" This is normal ", TextType.TEXT),
            TextNode("This is bold.", TextType.BOLD),
        ]

        #Call the split node selimter function
        actual_output = split_nodes_delimiter([node], "**", TextType.BOLD)

        #Assert equality
        self.assertEqual(actual_output, expected_output)

    def test_leading_delimiter(self):
        # Input a single TextNode wtih one set of properly paired bold delimiters at the start of the node
        node = TextNode("**This is bold** This is normal", TextType.TEXT)

        # Expected output. Split into two nodes with a leading bold node.
        expected_output = [
            TextNode("This is bold", TextType.BOLD),
            TextNode(" This is normal", TextType.TEXT),
        ]

        # Call the gplit_node_delimiter_function
        actual_output = split_nodes_delimiter([node], "**", TextType.BOLD)

        # Assert equality
        self.assertEqual(actual_output, expected_output)

    def test_trailing_delimiter(self):
        # Input a single TextNode wtih one set of properly paired bold delimiters at the end of the node
        node = TextNode("This is normal. **This is bold**", TextType.TEXT)

        # Expected output. Split into two nodes with a leading bold node.
        expected_output = [
            TextNode("This is normal. ", TextType.TEXT),
            TextNode("This is bold", TextType.BOLD),
        ]

        # Call the gplit_node_delimiter_function
        actual_output = split_nodes_delimiter([node], "**", TextType.BOLD)

        # Assert equality
        self.assertEqual(actual_output, expected_output)

    def test_double_delimiter(self):
        # Input a TextNode with two sets of properly paired bold delimiters on the same text
        node = TextNode("This is normal. ** **This is bold** ** This is normal.", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)

        # Check if the exception message matches
        self.assertEqual(
            str(context.exception), "Invalide Markdown Syntax: Must have text in between opening and closing **")
        
    def test_image_extraction(self):
        # Input a string with markdown for image embedded
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        # Expected output: A list of tuples consisting of the alt text and url of the image
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        # Assert equality
        self.assertEqual(extract_markdown_images(text), expected_output)

    def test_link_extraction(self):
        # Input a string with markdown for links embedded
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        # Expected output: A list of tuples consisting of the anchor text and url of the image
        expected_output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        # Assert equality
        self.assertEqual(extract_markdown_links(text), expected_output)

    def test_image_no_alt_text_extraction(self):
        # Input a string with markdown for image embedded with no alt text
        text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif) and ![](https://i.imgur.com/fJRm4Vk.jpeg)"

        # Expected output: A list of tuples consisting of the alt text and url of the image
        expected_output = [("", "https://i.imgur.com/aKaOqIh.gif"), ("", "https://i.imgur.com/fJRm4Vk.jpeg")]

        # Assert equality
        self.assertEqual(extract_markdown_images(text), expected_output)

    def test_split_images(self):
        # Input a TextNode with multiple images
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        

        # Expected output: A list of new TextNodes with the text in TEXT format and the image in IMAGE format
        expected_output = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ]

        # Assert equality
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_images_no_image(self):
        # Insert a TextNode with no images
        node = TextNode("This is a test with no image.", TextType.TEXT)

        # Expected output: Return a list with the TextNode only
        expected_output = [TextNode("This is a test with no image.", TextType.TEXT)]

        # Assert equality
        self.assertEqual([node], expected_output)

    def test_split_images_leading(self):
        # Input a TextNode with multiple images
        node = TextNode(
            "![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        

        # Expected output: A list of new TextNodes with the text in TEXT format and the image in IMAGE format
        expected_output = [
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ]

        # Assert equality
        self.assertEqual(split_nodes_image([node]), expected_output)   
    
    def test_split_images_trailing(self):
        # Input a TextNode with multiple images
        node = TextNode(
            "This is a trailing image ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        

        # Expected output: A list of new TextNodes with the text in TEXT format and the image in IMAGE format
        expected_output = [
            TextNode("This is a trailing image ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ]

        # Assert equality
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_imaages_back_to_back(self):
        # input a TextNode with no string in between two images
        node = TextNode("![first image](https://imageone.test)![second image](https://imagetwo.test)", TextType.TEXT)

        # Expected ouput: A list of two TextNodes with TextType.IMAGE
        expected_output = [
            TextNode("first image", TextType.IMAGE, "https://imageone.test"),
            TextNode("second image", TextType.IMAGE, "https://imagetwo.test"),
        ]

        #Assert equality
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_images_empty(self):
        # Input an empty TextNode
        node = TextNode("", TextType.TEXT)

        # Expected output: Empty list due to base case
        expected_output = []

        # Assert Equality
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_images_image_and_link(self):
        # Input a TExtNode that has both an image and link inside of it.
        node = TextNode(
            "This node has an image and a link. ![first image](https://imageone.test) and [link one](https://linkone.test)", TextType.TEXT
        )

        # Expected output: A text node with text, a text node with image and a text node with text contatinging the link unchanged
        expected_output = [
            TextNode("This node has an image and a link. ", TextType.TEXT),
            TextNode('first image', TextType.IMAGE, "https://imageone.test"),
            TextNode(" and [link one](https://linkone.test)", TextType.TEXT)
        ]

        # Assert equality
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_images_malformed_image(self):
        # Input a textNode that has a malformed image link
        node = TextNode("This has a broken image in it ![image one (https://imageone.text)", TextType.TEXT)

        # Expected output: A list with an unchanged textNode
        expected_output = [
            TextNode("This has a broken image in it ![image one (https://imageone.text)", TextType.TEXT),
        ] 
        
        # Assert equality
        self.assertEqual(split_nodes_image([node]), expected_output)

    def test_split_images_list_input(self):
        # INput a list with multiple TextNode objects
        node = [
            TextNode("This is a node with an image ![image one](https://imageone.test)", TextType.TEXT),
            TextNode("This is a second node with an image ![image two](https://imagetwo.text)", TextType.TEXT),
        ]

        # Expected output: A list with all the nodes
        expected_output = [
            TextNode("This is a node with an image ", TextType.TEXT),
            TextNode("image one", TextType.IMAGE, "https://imageone.test"),
            TextNode("This is a second node with an image ", TextType.TEXT),
            TextNode("image two", TextType.IMAGE, "https://imagetwo.text"),
        ]

        # Assert equality
        self.assertEqual(split_nodes_image(node), expected_output)

    def test_split_links(self):
        # INput a textNode that contains a link
        node = TextNode("This is a TextNode that containg a link to [Google](https://www.google.com)", TextType.TEXT)

        # Exptected output: A list with a TEXT type node and a LINK type node
        expected_output = [
            TextNode("This is a TextNode that containg a link to ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com"),
        ]

        # Assert equlity
        self.assertEqual(split_nodes_links([node]), expected_output)

if __name__ == "__main__":
    unittest.main()
        
