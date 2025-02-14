from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

# Enum representing different types of inline text elements in markdown
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode:
    """Represents an inline text element in markdown with its formatting and optional URL"""
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """Returns True if all properties of both nodes are equal"""
        if isinstance(other, TextNode):
            return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
            )
        return False

    def __repr__(self):
        """Returns string representation of the TextNode"""
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"    
    
def text_node_to_html_node(text_node):
    
    """Turns a TextNode object into a LeafNode based on the type of TextNode"""
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text,text_node.props["href"] )
        case TextType.IMAGES:
            return LeafNode("img", "", text_node["src", "alt"])
        case _:
            raise Exception(f"Invalid text type: {text_node.text_type}")
        


