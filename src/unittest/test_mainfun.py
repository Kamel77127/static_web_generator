import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from main import text_node_to_html,split_node_delimiter,extract_markdown_images
from TextNode import TextNode,TextType




class TestMainFunc(unittest.TestCase):
    
    
    
    def test(self):
        node = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpe)"
        html_node = extract_markdown_images(node)
        print(html_node)
   