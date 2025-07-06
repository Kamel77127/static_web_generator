from enum import Enum
import re
from Htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
    
    
    
class TextNode():
    
    
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
        
    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, { self.text_type.value}, {self.url})"        
    
    
TEXT_TYPE = {
    TextType.TEXT : lambda node: LeafNode(None,node.text),
    TextType.BOLD : lambda node: LeafNode("b",node.text),
    TextType.ITALIC : lambda node: LeafNode("i",node.text),
    TextType.CODE : lambda node: LeafNode("code",node.text),
    TextType.LINK : lambda node: LeafNode("a",node.text,{"href":node.url}),
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
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def split_nodes_image(old_nodes):
    
    new_nodes = []

    for node in old_nodes:
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) <= 0:
            new_nodes.append(node)
            continue
        for image in images:
            section = original_text.split(f"![{image[0]}]({image[1]})")
            
            if len(section) < 2:
                raise ValueError("Delimiter not closed")
            if section[0].strip():
                new_nodes.append(TextNode(section[0],TextType.TEXT))
            new_nodes.append(
                TextNode(image[0],TextType.IMAGE,image[1])
            )
            original_text = section[1]
                
        if original_text != "":
            new_nodes.append(TextNode(original_text,TextType.TEXT,None))  
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        original_text = node.text
        links = extract_markdown_links(original_text)
        
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            section = original_text.split(f"[{link[0]}]({link[1]})") 
            if len(section) < 2:
                raise ValueError("Delimiter not closed")
            if section[0].strip():
                new_nodes.append(TextNode(section[0],TextType.TEXT))
            new_nodes.append(TextNode(
                link[0],
                TextType.LINK,
                link[1]
            ))
            original_text = section[1]  
            
        if original_text != "":
            new_nodes.append(TextNode(original_text,TextType.TEXT,None)) 
    return new_nodes  


def text_to_textnodes(text):
    
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_node_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_node_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_node_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

     