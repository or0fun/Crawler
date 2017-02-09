
class Behavior(object):
    """docstring for Comment"""
    def __init__(self, comments, views):
        super(Behavior, self).__init__()
        self.comments = comments
        self.views = views
        
class Tag(object):
    tag = 0
    attrs = []
    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = attrs
    pass

class Info(object):
    title = ""
    date = ""
    site = ""
    link = ""
    children = ""
    behavior = Behavior(0, 0)
