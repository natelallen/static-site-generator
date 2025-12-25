class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
        
    def props_to_html(self):
        if self.props is None:
            return ""
        value = ""
        for prop in self.props:
            value += f' {prop}="{self.props[prop]}"'
        return value
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: LeafNode has no value attribute assigned")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: ParentNode has no tag value assigned")
        if self.children is None:
            raise ValueError("Invalid HTML: ParentNode is missing a children value")
        childrentags = ""
        for child in self.children:
            childrentags += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{childrentags}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
