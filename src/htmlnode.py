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
        #Check for no props or empty props
        if self.props == None or self.props == {}:
            return output
        #Create properties string and output
        for prop in self.props:
            output = output + f' {prop}="{self.props[prop]}"'
        return output
    
    def __repr__(self):
        """Returns string representation of the HTMLNode"""
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    """Represents a single HTML tag with no children"""

    def to_html(self):
        #Raises exception if no value
        if self.value == None:
            raise ValueError("Must have a value")
        #Returns plain text if no tag
        if self.tag == None:
            return f"{self.value}"
        #returns node with tag and properties
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
                