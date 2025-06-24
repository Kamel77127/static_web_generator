import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from main import text_node_to_html,split_node_delimiter
from TextNode import TextNode,TextType




class TestMainFunc(unittest.TestCase):
    
    
    
    def test(self):
        node = TextNode("This **is** a text **node**", TextType.BOLD)
        html_node = split_node_delimiter([node],"**",TextType.BOLD)
        print(html_node)
   