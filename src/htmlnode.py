class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """Represents an inline HTML tag and it's properties which are all optional"""
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """To be overidden by children classes"""
        raise NotImplementedError
    
    def props_to_html(self):
        """Returns a string that represents the HTML atributes of the node"""
        output = ""
        for prop in self.props:
            output = output + f' {prop}={self.props[prop]}'
        return output
    
    def __repr__(self):
        """Returns string representation of the HTMLNode"""
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"    