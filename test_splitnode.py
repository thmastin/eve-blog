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
    

    def test_placeholder(self):
        pass

if __name__ == "__main__":
    unittest.main()
        
