import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Htmlnode import ParentNode,LeafNode





class TestParentNode(unittest.TestCase):
    
    
    
    
    def test_to_html(self):
        leafnodes = [
        LeafNode("img", "Bold text"),
        LeafNode("a", "link text",{"href": "http//www.kamel.fr","target":"blank"}),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ]
        node1 = ParentNode("p",leafnodes)
        print(node1.to_html())
        
        





if __name__ == "__main__":
    unittest.main()