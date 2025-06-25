import sys
import os
import re
sys.path.append(os.path.join(os.path.dirname(__file__),"src/"))
from TextNode import TextType,TextNode
from Htmlnode import LeafNode


TEXT_TYPE = {
    TextType.TEXT : lambda node: LeafNode(None,node.text),
    TextType.BOLD : lambda node: LeafNode("b",node.text),
    TextType.ITALIC : lambda node: LeafNode("i",node.text),
    TextType.CODE : lambda node: LeafNode("code",node.text),
    TextType.LINK : lambda node: LeafNode("a",node.text),
    TextType.IMAGE : lambda node: LeafNode("img","",{"src":node.url,"alt":node.text})
}







def text_node_to_html(text_node):
    if text_node.text_type not in TEXT_TYPE:
        raise Exception("Not in available types")

    return TEXT_TYPE[text_node.text_type](text_node)
    
    
        
def split_node_delimiter(old_nodes,delimiter, text_type):
    final_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final_nodes.append(old_node)
            continue
        splitted = old_node.text.split(delimiter)
        if len(splitted) % 2 == 0:
            raise Exception("delimiter not closed")
        for i in range(len(splitted)):
            if splitted[i] == "":
                continue
            if i % 2 == 0:
                final_nodes.append(TextNode(splitted[i],TextType.TEXT))
            else:
                final_nodes.append(TextNode(splitted[i],text_type))
    return final_nodes
                
    

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    print(type(matches))
    return matches


def extract_markdown_links(text):
    
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\([([^\(\)]]*)\)")
    return matches