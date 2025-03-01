import unittest
import logging

from markdownblocks import markdown_to_blocks

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestSplitNodes(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        # Strip whitespace and log the input
        md_stripped = md.strip()
        logger.debug(f"Input markdown:\n{md_stripped}")
        
        # Call the function under test
        blocks = markdown_to_blocks(md)
        
        # Log the actual output
        logger.debug(f"Actual blocks output:\n{blocks}")
        
        # Expected output
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        
        # Log the expected output
        logger.debug(f"Expected blocks:\n{expected}")
        
        # Add detailed comparison for debugging
        for i, (actual, expect) in enumerate(zip(blocks, expected)):
            logger.debug(f"Block {i}:\nActual: {actual}\nExpected: {expect}")
            assert actual == expect, f"Mismatch at block {i}: expected '{expect}', got '{actual}'"
        
        # Print lengths for additional insight
        print(f"Number of blocks: {len(blocks)}")
        print(f"Number of expected blocks: {len(expected)}")
        
        # The original assertion
        self.assertEqual(
            blocks,
            expected,
            "The markdown blocks did not match the expected output"
        )

if __name__ == "__main__":
    unittest.main()