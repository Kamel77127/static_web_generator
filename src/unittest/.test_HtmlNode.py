import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Htmlnode import HTMLNode




class testHTMLNode(unittest.TestCase):
    
    
    
    def test_props_to_html(self):
        node = HTMLNode("a","http://www.kamel.fr",None,{"href": "http://www.kamel.fr", "target": "blank"})
        expected = ' href="http://www.kamel.fr" target="blank"'
        val = node.props_to_html()
        self.assertEqual(val,expected)
        
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    unittest.main()