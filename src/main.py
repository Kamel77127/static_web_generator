import sys
import os
import re
import shutil
sys.path.append(os.path.join(os.path.dirname(__file__),"src/"))
from TextNode import TextType,TextNode
from Htmlnode import LeafNode
from BlockType import markdown_to_html_node
from pathlib import Path
 
 
 
 
 

      
def static_to_public_path(dest_dir):
    public_path = dest_dir
    static_path = os.path.join(os.path.dirname(__file__),"../static")
    
    
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
        
#######    
def extract_title(markdown):
    if not "h1" in markdown:
        raise Exception("No Header 1 found")
    return re.findall(r"[^<h1>].*?[^</h1>]",markdown)[0]

#######
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



#####

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    if os.listdir(dir_path_content):
        
        src_path = Path(dir_path_content)
        tp_path = Path(template_path)
        dest = Path(dest_dir_path)
        
        with tp_path.open('r') as tp_file:
            tp_files = tp_file.read()
        
        dest.mkdir(parents=True,exist_ok=True)

        for content in src_path.iterdir():
            
            dest_content = dest / content.name            
            if content.is_file() and content.suffix == ".md":
                
                dest_file = dest_content.with_suffix('.html')
                
                with content.open('r') as file:
                    copied_file = file.read()
                
                html_content = markdown_to_html_node(copied_file).to_html()
                title = extract_title(html_content)
                tp_files = tp_files.replace('{{ Title }}', title).replace('{{ Content }}',html_content)
                print(basepath)
                with dest_file.open('w') as dest_file:
                    dest_file.write(tp_files)
                
            elif content.is_dir():
                print(f"This content : {content} is not a dir")
                generate_pages_recursive(content,tp_path,dest_content,basepath)
    
    ## il faut que j'améliore extract title
    ## il faut que j'ajoute pre code
    
    
script_dir = os.path.dirname(__file__)
dir_path_content = os.path.join(script_dir, "../content")
template_path = os.path.join(script_dir,"../template.html")

if len(sys.argv) >= 2:
    basePath = os.path.join(script_dir,".." + sys.argv[1])
else:
    basePath = os.path.join(script_dir,"../")

des_dir_content = os.path.join(script_dir, "../docs")
## for generate recursive path :
generate_pages_recursive(dir_path_content,template_path,des_dir_content, basePath)
static_to_public_path(des_dir_content)   
