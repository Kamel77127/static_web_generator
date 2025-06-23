import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from Htmlnode import LeafNode





class TestLeafNode(unittest.TestCase):
    
    
    
    def test_to_html(self):
        node = LeafNode("a","http://www.kamel.fr",{"href": "http://www.kamel.fr", "target": "blank"})
        print(node.to_html())
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()