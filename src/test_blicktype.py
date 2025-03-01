import unittest

from blocktype import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_heading(self):
        block = "### this is a heading"
        block_type = block_to_block_type(block)

        self.assertIs(block_type, BlockType.HEADING)
    
    def test_code(self):
        block = "```this is code```"
        block_type = block_to_block_type(block)

        self.assertIs(block_type, BlockType.CODE)

    def test_quote(self):
        block = ">this is line one\n>this is line two\n>this is line three"
        block_type = block_to_block_type(block)

        self.assertIs(block_type, BlockType.QUOTE)
    
    def test_unordered_list(self):
        block = "- this is line one\n- this is line two\n- this is line three"
        block_type = block_to_block_type(block)

        self.assertIs(block_type, BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        block = "1. line one\n2. line two\n3. line three"
        block_type = block_to_block_type(block)

        self.assertIs(block_type, BlockType.ORDERED_LIST)

    

if __name__ == "__main__":
    unittest.main()