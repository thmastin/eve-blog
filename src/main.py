from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from copydirectory import copy_directory
from generatepage import generate_page

def main():
    copy_directory("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()