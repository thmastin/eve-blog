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
                


        