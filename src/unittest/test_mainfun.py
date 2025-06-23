import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from main import text_node_to_html
from TextNode import TextNode,TextType




class TestMainFunc(unittest.TestCase):
    
    
    
    def test(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html(node)
        print(html_node)
   