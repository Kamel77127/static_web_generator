












class HTMLNode():
    
    
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
        
        
    def to_html(self):
        raise NotImplemented()
    
    def props_to_html(self):
        props_tp_html = ""
        if self.props != None:
            for prop in self.props:
                props_tp_html += f' {prop}="{self.props[prop]}"'
        return props_tp_html
    def __repr__(self):
        return f"HTMLNode({self.tag}, { self.value}, {self.children}, {self.props})" 
    
    
    
    
    
    
    
    
    
    
    
class LeafNode(HTMLNode):
        
        
        
    def __init__(self,tag,value,props=None):
        super().__init__(tag=tag,value=value,children=None,props=props)
        self.tag = tag
        self.value=value
        self.props=props
        
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode should have a value")
        if self.tag == None:
            return f"{self.value}"
        else:
            return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'
        
        
        
        
class ParentNode(HTMLNode):
    
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        self.tag = tag
        self.children = children
        self.props = props
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag nécessaire")
        if self.children == None:
            raise ValueError("Children absent")
        text = ""
        for child in self.children:
            text += child.to_html()
        return f'<{self.tag}>' + text + f'</{self.tag}>'
        