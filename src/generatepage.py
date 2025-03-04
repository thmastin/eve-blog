from markdowntohtmlnode import markdown_to_html_node
import os

def extract_title(markdown):    
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.strip("# ")
    raise Exception("No heading in markdown file")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    
    #Open files and create strings
    with open(from_path) as f:
        page_string = f.read()
    
    with open(template_path) as f:
        template_string = f.read()

    page_node = markdown_to_html_node(page_string)
    page_html = page_node.to_html()

    page_title = extract_title(page_string)

    final_page = template_string.replace("{{ Title }}", page_title)
    final_page = final_page.replace("{{ Content }}", page_html)

    if not os.path.exists(dest_path):
        os.mkdirs(dest_path)
    
    with open(dest_path, "w") as f:
        f.write(final_page)
    


