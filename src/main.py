from textnode import TextNode, TextType

def main():
    #Create a test node and print it to verify TextNode implmentation
    textnode = TextNode("This is a text node", TextType.BOLD, "https://example.com")
    print(textnode)

if __name__ == "__main__":
    main()