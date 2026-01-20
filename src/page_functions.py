from node_functions import markdown_to_html_node
import os
import re

def extract_title(markdown):
    heading_search = re.compile(r"^# [\w\d \,\.&]+", flags=re.MULTILINE)
    headings = heading_search.search(markdown)
    if headings is None:
        raise Exception("Markdown has no header for title.")
    return headings[0].lstrip().lstrip("# ")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, encoding='utf-8') as md_file:
        markdown = md_file.read()
    
    with open(template_path, encoding="utf-8") as template_file:
        template = template_file.read()

    content = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)
    full_html_page = template.replace("{{ Title }}", page_title).replace("{{ Content }}", content)

    with open(dest_path, encoding="utf-8", mode="w+") as output_file:
        output_file.write(full_html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for object in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, object)
        dest_path = os.path.join(dest_dir_path, object)
        if os.path.isfile(source_path):
            dest_path = dest_path.replace('.md', '.html')
            generate_page(source_path, template_path, dest_path)
        else:
            os.mkdir(dest_path)
            generate_pages_recursive(source_path, template_path, dest_path)
        
        