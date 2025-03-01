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
    
    def test_paragraph(self):
        block = "This is a paragraph"
        block_type = block_to_block_type(block)

        self.assertIs(block_type, BlockType.PARAGRAPH)
    
    def test_broken_ordered_list(self):
        block = "1. line one\n3. line 3"
        block_type = block_to_block_type(block)

        self.assertIs(block_type, BlockType.PARAGRAPH)
    
    def test_max_heading(self):
        block = "###### this is a max heading"
        self.assertIs(block_to_block_type(block), BlockType.HEADING)

    def test_heading_too_large(self):
        block = "####### this should be a paragraph"
        self.assertIs(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_no_space(self):
        block = "#This should be a paragraph"
        self.assertIs(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_empty_block(self):
        block = ""
        self.assertIs(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_empty_code_block(self):
        block = "``````"
        self.assertIs(block_to_block_type(block), BlockType.CODE)
    
    def test_code_block_with_embedded_other_code(self):
        block = "```# This is a heading```"
        self.assertIs(block_to_block_type(block), BlockType.CODE)
    
    def test_code_no_closing(self):
        block = "```code block"
        self.assertIs(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_quote_mulitple_lines(self):
        block = ">First Line\n>SecondLine"
        self.assertIs(block_to_block_type(block), BlockType.QUOTE)


    

if __name__ == "__main__":
    unittest.main()