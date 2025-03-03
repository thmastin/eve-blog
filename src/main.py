from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from copydirectory import copy_directory

def main():
    copy_directory("static", "public")

if __name__ == "__main__":
    main()