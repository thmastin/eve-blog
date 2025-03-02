from markdownblocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from textnode import text_node_to_html_node, TextNode, TextType
from splitnode import text_to_textnodes
from htmlnode import ParentNode

def markdown_to_html_node(markdown):
    # Split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    output_blocks = []
 
    for block in blocks:
        # Determine type of block
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            modified_block = block.replace("\n", " ")
            output_blocks.append(ParentNode("p", text_to_children(modified_block)))
        elif block_type == BlockType.CODE:
            output_blocks.append(process_code_block(block))
    return ParentNode("div", output_blocks)

def text_to_children(text):
    output_nodes = []
    nodes = text_to_textnodes(text)
    
    for node in nodes:
        output_nodes.append(text_node_to_html_node(node))
    
    return output_nodes

def process_code_block(block):
    lines = block.split("\n")
    # Make sure to include the final newline that the test expects
    code_content = "\n".join(lines[1:-1]) + "\n"
    
    text_node = TextNode(code_content, TextType.TEXT)
    code_html_node = text_node_to_html_node(text_node)
    
    code_node = ParentNode("code", [code_html_node])
    pre_node = ParentNode("pre", [code_node])
    return pre_node