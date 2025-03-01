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

    

if __name__ == "__main__":
    unittest.main()