import unittest
from markdowntohtmlnode import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
    # This is a heading

    ## This is a subheading

    ### This is a level 3 heading with **bold** text
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><h2>This is a subheading</h2><h3>This is a level 3 heading with <b>bold</b> text</h3></div>",
        )

    def test_quote_block(self):
        md = """
    > This is a quote
    > with multiple lines
    > and some **bold** text
    > and some _italic_ text
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines and some <b>bold</b> text and some <i>italic</i> text</blockquote></div>",
        )
    
    def test_ordered_list(self):
        md = """
    1. First item
    2. Second item with **bold**
    3. Third item with _italic_
    4. Fourth item with `code`
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i></li><li>Fourth item with <code>code</code></li></ol></div>",
        )

    def test_unordered_list(self):
        md = """
    - First item in the list
    - Second item with **bold** text
    - Third item with _italic_ text
    - Fourth item with `code` elements
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item in the list</li><li>Second item with <b>bold</b> text</li><li>Third item with <i>italic</i> text</li><li>Fourth item with <code>code</code> elements</li></ul></div>"
        )

    def test_comprehensive_markdown(self):
        markdown = "# Heading Level 1\n\nThis is a paragraph with **bold** and _italic_ text.\n\n## Heading Level 2\n\n- List item 1\n- List item 2\n- List item 3\n\n1. Ordered item 1\n2. Ordered item 2\n3. Ordered item 3\n\n> This is a blockquote\n> with multiple lines\n\n```\ndef hello_world():\n    print(\"Hello, world!\")\n```\n\nFinal paragraph here."
        
        expected = "<div><h1>Heading Level 1</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><h2>Heading Level 2</h2><ul><li>List item 1</li><li>List item 2</li><li>List item 3</li></ul><ol><li>Ordered item 1</li><li>Ordered item 2</li><li>Ordered item 3</li></ol><blockquote>This is a blockquote with multiple lines</blockquote><pre><code>def hello_world():\n    print(\"Hello, world!\")\n</code></pre><p>Final paragraph here.</p></div>"
        
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, expected)

if __name__ == "__main__":
    unittest.main()