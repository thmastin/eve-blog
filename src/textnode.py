from enum import Enum

# Enum representing different types of inline text elements in markdown
class TextType(Enum):
    NORMAL = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
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