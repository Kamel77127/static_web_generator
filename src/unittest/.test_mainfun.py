import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from main import text_node_to_html,split_node_delimiter,extract_markdown_images,split_nodes_image,static_to_public_path
from TextNode import TextNode,TextType




class TestMainFunc(unittest.TestCase):
    
    
    
    def test(self):
        static_to_public_path()
                