import sys
import os
import re
import shutil
sys.path.append(os.path.join(os.path.dirname(__file__),"src/"))
from TextNode import TextType,TextNode
from Htmlnode import LeafNode
from BlockType import markdown_to_html_node

 
      
def static_to_public_path():
    public_path = os.path.join(os.path.dirname(__file__),"../public")
    static_path = os.path.join(os.path.dirname(__file__),"../static")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    
    def copy_src_to_dst(src,dst):
        
        for item in os.listdir(src):
            src_item = os.path.join(src,item)
            dst_item = os.path.join(dst,item)
            if os.path.isfile(src_item):
                shutil.copy(src_item,dst)
                return
            elif os.path.isdir(src_item):
                os.mkdir(os.path.join(dst,item))
                copy_src_to_dst(src_item,dst_item)
       
    return copy_src_to_dst(static_path , public_path)   
        
        
def extract_title(markdown):
    if not "h1" in markdown:
        raise Exception("No Header 1 found")
    return re.findall(r"<h1\b[^>]*>.*?</h1>",markdown)[0]

def generate_page(from_path, template_path, dest_path):
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as from_path_file:
        fp_data = from_path_file.read()
    
    with open(template_path) as template_file:
        tp_data = template_file.read()   
                 
    parsed_markdown = markdown_to_html_node(fp_data).to_html()
    title_page = extract_title(parsed_markdown)
    tp_data = tp_data.replace('{{ Title }}',title_page).replace('{{ Content }}', parsed_markdown)
    
    
    
    with open(dest_path , "w") as destination_path:
        destination_path.write(tp_data)
    