from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith("#"):
        # Count consecutive # symbols
        hash_count = 0
        for char in block:
            if char == '#':
                hash_count += 1
            else:
                break
                
        # Valid heading: 1-6 # followed by a space
        if 1 <= hash_count <= 6 and len(block) > hash_count and block[hash_count] == ' ':
            return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif True:
        lines = block.split("\n")
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                break
            i += 1
        else: 
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH