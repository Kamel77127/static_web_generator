import sys
import os
import unittest


sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from BlockType import block_to_block_type,markdown_to_html_node,markdown_to_blocks
from main import extract_title,generate_page




class TestBlock(unittest.TestCase):
    
    
    
    def test(self):
        
        md = """

This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)

"""
        
        result =  markdown_to_html_node(md)
        fp_p = os.path.join(os.path.dirname(__file__), "../../content/index.md")
        ds_p = os.path.join(os.path.dirname(__file__), "../../public/index.html")
        tp_p = os.path.join(os.path.dirname(__file__), "../../template.html")
        ##print(result.to_html())
        generate_page(fp_p,tp_p,ds_p)     
        
        
        
        
if __name__ == "__main__":
    unittest.main()