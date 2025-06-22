import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from TextNode import TextNode, TextType




class TestTextNode(unittest.TestCase):
    
    def testeq(self):
        node1 = TextNode("charabia", TextType.BOLD)
        node2 = TextNode("charabia", TextType.BOLD)
        
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1,node2)
        
        
        
if __name__ == "__main__":
    unittest.main()
