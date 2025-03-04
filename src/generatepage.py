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

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(final_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
        
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        
        if os.path.isfile(src_path) and src_path.endswith(".md"):
            # Change the extension from .md to .html
            dest_file = item.replace(".md", ".html")
            dest_path = os.path.join(dest_dir_path, dest_file)
            generate_page(src_path, template_path, dest_path)
        elif os.path.isdir(src_path):
            # Create subdirectory in destination
            sub_dest_dir = os.path.join(dest_dir_path, item)
            if not os.path.exists(sub_dest_dir):
                os.makedirs(sub_dest_dir)
            # Recursive call with updated source and destination paths
            generate_pages_recursive(src_path, template_path, sub_dest_dir)


