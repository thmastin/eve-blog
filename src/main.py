from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    #Create a test node and print it to verify TextNode implmentation
    textnode = TextNode("This is a text node", TextType.BOLD, "https://example.com")
    print(textnode)
    leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leafnode)

if __name__ == "__main__":
    main()