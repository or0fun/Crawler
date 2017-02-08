

from tag import Tag
from tag import Info

from HTMLParser import HTMLParser

class BdResultsParser(HTMLParser):

    def __init__(self):   
        HTMLParser.__init__(self)   
        self.results = []
        self.isResult = False
        self.isCTitle = False
        self.tags = []

        self.info = Info()
        self.title_tmp = ""

    def is_result_title(self,tag,attrs):
        if tag == 'div' and attrs:
            for key, value in attrs:
                if key == 'class' and value == 'result title':
                    return True
        return False

    def is_c_title(self,tag,attrs):
        if False == self.isResult:
            return False
        if tag == 'h3' and attrs:
            for key, value in attrs:
                if key == 'class' and value == 'c-title':
                    return True
        return False

    def handle_starttag(self,tag,attrs):

        self.tags.append(Tag(tag, attrs))

        if self.is_result_title(tag, attrs):
            self.isResult = True
            self.info = Info()
            pass
        if self.is_c_title(tag, attrs):
            self.isCTitle = True
            pass

    def handle_startendtag(self,tag,attrs):
        pass

    def handle_endtag(self,tag):
        tag = self.tags.pop()
        if self.is_result_title(tag.tag, tag.attrs):
            self.isResult = False
            self.results.append(self.info)
            pass

        if self.isResult:
            if self.is_c_title(tag.tag, tag.attrs):
                self.isCTitle = False
                self.info.title = self.title_tmp
                self.title_tmp = ""

    def handle_data(self,data):
        if self.isCTitle:
            self.title_tmp += data
         