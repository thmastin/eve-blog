import unittest

from splitnode import split_nodes_delimiter
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
        # Input a single TextNode wtih one set of properly paired bold delimiters at the start of the node
        node = TextNode("This is normal. **This is bold**", TextType.TEXT)

        # Expected output. Split into two nodes with a leading bold node.
        expected_output = [
            TextNode("This is normal. ", TextType.TEXT),
            TextNode("This is bold", TextType.BOLD),
        ]

        # Call the gplit_node_delimiter_function
        actual_output = split_nodes_delimiter([node], "**", TextType.BOLD)

        # Assert equality2
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
        
