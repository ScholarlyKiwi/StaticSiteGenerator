from enum import Enum, auto
import re

class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = auto()
    CODE = auto()
    QUOTE = auto()
    UNORDERED_LIST = auto()
    ORDERED_LIST = auto()

def block_to_block_type(markdown_block):
    markdown_lines = markdown_block.splitlines()
    num_lines = len(markdown_lines)
    if re.match(r"#{1,6} ", markdown_block):
        return BlockType.HEADING
    elif re.match("```",markdown_block) and re.search("```$", markdown_block):
        return BlockType.CODE
    else:
        quote_block = True
        unordered_list = True
        ordered_list = True

        for line in markdown_lines:
            if not line.startswith(r">"):
                quote_block = False
            if not re.match(r"- ", line):
                unordered_list = False
        if quote_block:
            return BlockType.QUOTE
        if unordered_list:
            return BlockType.UNORDERED_LIST
        
        line_number = 1
        for line in markdown_lines:
            if not re.match(f"^{line_number}. ", line):
                ordered_list = False
            line_number += 1
        if ordered_list:
            return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH
