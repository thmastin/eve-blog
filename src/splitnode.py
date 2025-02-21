import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Splits a list of text nodes into individual nodes"""
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else: 
            is_delimited = False
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception(f"Invalid Markdown Syntax: Must have closing {delimiter}")
            for part in parts:
                if not is_delimited:
                    if part != "":
                        new_nodes.append(TextNode(part, TextType.TEXT))
                    is_delimited = True
                else:
                    stripped_part = part.strip()
                    if stripped_part == "":
                        raise Exception(f"Invalide Markdown Syntax: Must have text in between opening and closing {delimiter}")
                    else:
                        new_nodes.append(TextNode(part, text_type))
                        is_delimited = False
    return new_nodes
                
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        if extracted_images == []:
            if node.text != "":
                new_nodes.append(node)
        else:
            alt_text = extracted_images[0][0]
            url = extracted_images[0][1]
            split_node = node.text.split(f"![{alt_text}]({url})", 1)
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            remaining_node = TextNode(split_node[1], TextType.TEXT)
            new_nodes.extend(split_nodes_image([remaining_node]))
    return new_nodes

        