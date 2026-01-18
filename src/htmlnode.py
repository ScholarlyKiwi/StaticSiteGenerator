

class HTMLNode():

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        attributes = ''
        if not self.props:
            return attributes
        for attribute, value in self.props.items():
            attributes += f' {attribute}="{value}"'
        return attributes

    def __eq__(self, other):
        tag_matches = self.tag == other.tag
        value_matches = self.value == other.value
        children_matches = str(self.children) == str(other.children)
        props_matches = str(self.props) == str(self.props)
        return tag_matches and value_matches and children_matches and props_matches

    def __repr__(self):
        return str(f'HTMLNode({self.tag}, {self.value}, {str(self.children)}, {str(self.props)})')
