
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