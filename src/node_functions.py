from textnode import *
from leafnode import LeafNode
from htmlnode import HTMLNode
from blocktype import *
from parentnode import ParentNode
import re

def text_node_to_html_node(text_node):
    if type(text_node) != TextNode:
        raise Exception("text_node_to_html_code called on wrong type")
    if text_node.text_type not in TextType:
        raise Exception(f"Invalid TextType: {text_node.text_type}")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = list()
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        elif delimiter in old_node.text:
            if old_node.text.count(delimiter) % 2 > 0:
                raise ValueError(f"TextNode contains unclosed inline formatting for {delimiter}")
            else:
                in_delimiter = False
                sections = old_node.text.split(delimiter)
                for section in sections:
                    if len(section) == 0:
                        pass
                    elif in_delimiter:
                        new_nodes.append(TextNode(section, text_type))
                    else:
                        new_nodes.append(TextNode(section, TextType.TEXT))
                    in_delimiter = not in_delimiter

        else:
            new_nodes.append(old_node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = list()
    for old_node in old_nodes:
        html_tuples = extract_markdown_images(old_node.text)
        if len(html_tuples) == 0:
            new_nodes.append(old_node)
        else:
            original_text = old_node.text
            for (image_alt, image_link) in html_tuples:
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = sections[1]
            if len(original_text) > 0:
                new_nodes.append(TextNode(sections[1], TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = list()
    for old_node in old_nodes:
        html_tuples = extract_markdown_links(old_node.text)
        if len(html_tuples) == 0:
            new_nodes.append(old_node)
        else:
            original_text = old_node.text
            for (link_alt, link_url) in html_tuples:
                sections = original_text.split(f"[{link_alt}]({link_url})", 1)
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
                original_text = sections[1]
            if len(original_text) > 0:
                new_nodes.append(TextNode(original_text, TextType.TEXT))
            
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    return nodes

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        block = block.strip()
        if len(block) > 0:
            blocks.append(block)
    return blocks

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                blocknode = paragraph_block_to_html_node(block)
            case BlockType.HEADING:
                blocknode = heading_block_to_html_node(block)
            case BlockType.CODE:
                blocknode = code_block_to_html(block)
            case BlockType.QUOTE:
                blocknode = quote_block_to_html_node(block)
            case BlockType.UNORDERED_LIST:
                blocknode = unordered_list_block_to_html_node(block)
            case BlockType.ORDERED_LIST:
                blocknode = ordered_list_block_to_html_node(block)
        if blocknode:
            children.append(blocknode)
    return ParentNode("div", children)

def text_to_children(blocktext):
    blocktext = blocktext.replace("\n", " ")
    children = []
    text_nodes = text_to_textnodes(blocktext)
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    if len(children) > 0:
        return children
    else:
        return None

def code_block_to_html(blocktext):
    text = re.sub("```$", "", re.sub("^```", "", blocktext)).lstrip()
    return ParentNode("pre",[LeafNode("code", text)])

def paragraph_block_to_html_node(blocktext):
    children = text_to_children(blocktext)
    if len(children) > 0:
        return ParentNode("p", children)
    else:
        return None

def heading_block_to_html_node(blocktext):
    heading_level = len(blocktext) - len(blocktext.lstrip('#'))
    return ParentNode(f"h{heading_level}", text_to_children(blocktext.lstrip('#').lstrip()))

def quote_block_to_html_node(blocktext):
    text = blocktext.replace("> ", "").replace("\n", " ")
    return LeafNode("blockquote", text)

def unordered_list_block_to_html_node(blocktext):
    children = []
    for line in blocktext.splitlines():
        text = line.lstrip("- ")
        node = ParentNode("li", text_to_children(text))
        children.append(node)
    return ParentNode("ul", children)

def ordered_list_block_to_html_node(blocktext):
    children = []
    for line in blocktext.splitlines():
        text = re.sub(r"^\d*\. ", "", line)
        node = ParentNode("li", text_to_children(text))
        children.append(node)
    return ParentNode("ol", children)