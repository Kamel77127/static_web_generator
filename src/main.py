import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"src/"))
from TextNode import TextType
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
    
    
        
        