from textnode import TextType, TextNode

def main():
    node = TextNode("Hi", TextType.LINK, "https://www.google.com")
    print(node)

if __name__ == "__main__":
    main()