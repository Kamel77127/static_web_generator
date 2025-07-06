
from enum import Enum
from Htmlnode import ParentNode
from TextNode import text_node_to_html,text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

TAGS = {
    "paragraph" : "p",
    "heading" :"h",
    "code" : "code",
    "quote" : "quote",
    "unordered_list" : "li",
    "ordered_list" : "ol"
}



def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block.strip()]
                    
            



def block_to_block_type(blocks):
    lines= blocks.split("\n")
    empty_lines = [line.strip() for line in lines if line.strip()]
    
    if blocks.startswith(("#","##","###","####","#####","######")):
        return BlockType.HEADING
    if blocks.startswith("```") and blocks.endswith("```"):
        return BlockType.CODE
    if empty_lines and all(line.startswith(">") for line in lines if empty_lines):
        return BlockType.QUOTE
    if empty_lines and  all(line.startswith("- ") for line in lines if empty_lines):
        return BlockType.UNORDERED_LIST
    if empty_lines and  is_ordered_list(empty_lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH



def is_ordered_list(non_empty_lines):
    for i,line in enumerate(non_empty_lines, start=1):
        prefix = f"{i}. "
        if not line.startswith(prefix):
            return False
    return True
    
    
def markdown_to_html_node(markdown):
    block_section = markdown_to_blocks(markdown)
    parent_node = []
    c = 0
    for block in block_section:
        type = block_to_block_type(block)
        if type == BlockType.HEADING:
            count = block[0:7].count("#") 
            parsed_block = node_parser(block,type)
            parent_node.append(node_to_htmlnode(block_to_textnode(parsed_block),type,count=count))
        else : 
            parsed_block = node_parser(block,type)
            parent_node.append(node_to_htmlnode(block_to_textnode(parsed_block),type))
            
    
    return ParentNode("div",parent_node,None)
        
        
def block_to_textnode(text):
    result = []
    textNodes = text_to_textnodes(text)
    for text in textNodes:
        result.append(text_node_to_html(text))
    return result
    
def node_to_htmlnode(nodes,type=None,props=None,count=None):
    
                if type == BlockType.PARAGRAPH:
                    return ParentNode("p",nodes,None)
                if type == BlockType.HEADING:
                    return ParentNode(f"h{count}",nodes,None)
                if type == BlockType.CODE:
                    return ParentNode("pre",nodes,None)
                if type == BlockType.QUOTE:
                    return ParentNode("quote",nodes,None)
                if type == BlockType.UNORDERED_LIST:
                    return ParentNode("ul",nodes,None)
                if type == BlockType.ORDERED_LIST:
                    return ParentNode("ol",nodes,None)
    


def node_parser(node,type):
    if type == BlockType.HEADING:
        count = node[0:5].count("#")
        return node[count:]
    if type == BlockType.CODE:
        return node[3:-3]
    if type == BlockType.QUOTE:
        return node.strip(">")
    if type == BlockType.UNORDERED_LIST:
        lines = "".join(line.strip("- ") for line in node)
    if type == BlockType.ORDERED_LIST:
        lines = ""
        for i,line in enumerate(node.split("\n"),start=1):
            lines += "".join(line.strip(f"{i}. ")) + "\n"
        return lines
    return node
    
## je dois trouver un moyen de compter les # et les retourner