import unittest

from blocktype import *

class Test_block_type(unittest.TestCase):

    def test_block_type_heading(self):
        block = '# heading'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_type_code(self):
        block = """```
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
```"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_type_paragraph(self):
        block="Hello all"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_type_quote(self):
        block = """> This is an example of a block post
> With multiple lines.
> It is pretty basic thing."""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_type_unordered(self):
        block = """- Unorder List Item 1 
- Unorder List Item 2
- Unorder List Item 3
- Unorder List Item 4"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_type_ordered(self):
        block = """1. Order List Item 1 
2. Order List Item 2
3. Order List Item 3
4. Order List Item 4"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_type_ordered_mal(self):
        block = """1. Order List Item 1 
2. Order List Item 2
Order List Item 3
4. Order List Item 4"""
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_type_unordered_mal(self):
        block = """- Unorder List Item 1 
- Unorder List Item 2
Unorder List Item 3
- Unorder List Item 4"""
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_type_quote_mal(self):
        block = """> This is an example of a block post
With multiple lines.
> It is pretty basic thing."""
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.QUOTE)