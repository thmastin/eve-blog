from enum import Enum

class TextType(Enum):
    NORMAL = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGS = "image"

class Textnode(text, text_type, url=None):
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    
