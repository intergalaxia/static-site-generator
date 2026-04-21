class HTMLNode:
    def __init__(self,tag= None, value= None, children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        result = ""
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result
    
    def __repr__(self):
         return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props= None):
        super().__init__(tag,value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Need a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
         return f"HTMLNode({self.tag}{self.value}{self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required.")
        if self.children is None:
            raise ValueError("Children missing value.")
        result = ""
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
