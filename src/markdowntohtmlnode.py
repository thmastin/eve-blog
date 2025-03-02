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
            output_blocks.append(process_paragraph_block(block))
        elif block_type == BlockType.CODE:
            output_blocks.append(process_code_block(block))
        elif block_type == BlockType.HEADING:
            output_blocks.append(process_heading_block(block))
        elif block_type == BlockType.QUOTE:
            output_blocks.append(process_quote_block(block))
        elif block_type == BlockType.ORDERED_LIST:
            output_blocks.append(process_ordered_list_block(block))
        elif block_type == BlockType.UNORDERED_LIST:
            output_blocks.append(process_unordered_list_block(block))

    return ParentNode("div", output_blocks)

def text_to_children(text):
    output_nodes = []
    nodes = text_to_textnodes(text)
    
    for node in nodes:
        output_nodes.append(text_node_to_html_node(node))
    
    return output_nodes

def process_code_block(block):
    lines = block.split("\n")
    code_content = "\n".join(lines[1:-1]) + "\n"
    
    # Add this print statement
    
    text_node = TextNode(code_content, TextType.TEXT)
    code_html_node = text_node_to_html_node(text_node)
    
    code_node = ParentNode("code", [code_html_node])
    pre_node = ParentNode("pre", [code_node])
    return pre_node

def process_heading_block(block):
    words = block.split(" ")
    # Count # for tag
    heading_level = len(words[0])

    # Rejoin content without the # and leading space
    heading_content = " ".join(words[1:])

    # Handle inline html
    text_node = text_to_children(heading_content)

    heading_node = ParentNode(f"h{heading_level}", text_node)
    return heading_node

def process_quote_block(block):
    # Break block into lines
    lines = block.split("\n")
    new_lines = []

    # Remove leading "> " from each line"
    for line in lines:
        new_lines.append(line.strip("> "))
    
    # Join lines
    stripped_block = " ".join(new_lines)

    # Handle inlikne html
    text_node = text_to_children(stripped_block)

    quote_node = ParentNode("blockquote", text_node)
    return quote_node

def process_ordered_list_block(block):
    # break block into lines
    lines = block.split("\n")
    
    # Remove leading "(number). "
    new_lines = []
    list_nodes = []

    for line in lines:
        new_line = line.split(" ")
        new_lines.append(" ".join(new_line[1:]))

    # Process inline text for each new_line and create ParentNode
    for line in new_lines:
        list_nodes.append(ParentNode("li", text_to_children(line)))

    # Make outer node with <ol> tag
    ordered_list_node = ParentNode("ol", list_nodes)

    return ordered_list_node

def process_unordered_list_block(block):
    # break block into lines
    lines = block.split("\n")
    
    # Remove leading "(number). "
    new_lines = []
    list_nodes = []

    for line in lines:
        new_line = line.split(" ")
        new_lines.append(" ".join(new_line[1:]))

    # Process inline text for each new_line and create ParentNode
    for line in new_lines:
        list_nodes.append(ParentNode("li", text_to_children(line)))

    # Make outer node with <ol> tag
    unordered_list_node = ParentNode("ul", list_nodes)

    return unordered_list_node

def process_paragraph_block(block):
    modified_block = block.replace("\n", " ")

    paragraph_block = ParentNode("p", text_to_children(modified_block))
    return paragraph_block