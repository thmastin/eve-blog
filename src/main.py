from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from copydirectory import copy_directory
from generatepage import generate_pages_recursive

def main():
    copy_directory("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()