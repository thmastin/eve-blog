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
            raise ValueError("LeafNode mush have a value")
        #Returns plain text if no tag
        if self.tag == None:
            return f"{self.value}"
        #returns node with tag and properties
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    """Represents a parent HTML tag with children"""

    def to_html(self):
        # Ensure a tag exists
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        # Ensure children exist
        if self.children is None:
            raise ValueError("ParentNode must have children")

        # Recursively process children into a single HTML string
        child_html = "".join(child.to_html() for child in self.children)

        # Wrap the children in the current node's tags
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
        
                