

from tag import Tag
from tag import Info

from HTMLParser import HTMLParser

class BdResultsParser(HTMLParser):

    def __init__(self):   
        HTMLParser.__init__(self)   
        self.results = []
        self.isResult = False
        self.isCTitle = False
        self.isAuthor = False
        self.tags = []

        self.info = Info()
        self.title_tmp = ""

        self.lastTag = ""

    def is_result_title(self,tag,attrs):
        if tag == 'div' and attrs:
            for key, value in attrs:
                if key == 'class' and value.find('result title') > -1:
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

    def is_c_title_author(self,tag,attrs):
        if False == self.isResult:
            return False
        if tag == 'div' and attrs:
            for key, value in attrs:
                if key == 'class' and value == 'c-title-author':
                    return True
        return False

    def handle_starttag(self,tag,attrs):

        if self.is_result_title(tag, attrs):
            self.isResult = True
            self.info = Info()

        if self.isResult:
            self.tags.append(Tag(tag, attrs))
        else:
            return

        if self.is_c_title(tag, attrs):
            self.isCTitle = True
            return

        if self.isCTitle and tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    self.info.link = value
                    return

        if self.is_c_title_author(tag, attrs):
            self.isAuthor = True
            return

        if self.isAuthor and tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    if value.startswith('http'): 
                        self.info.children = value
                    else:
                        self.info.children = "http://news.baidu.com/" + value
                    return

    def handle_endtag(self,tag):

        if self.isResult == False:
            return

        tag = self.tags.pop()
        if self.is_result_title(tag.tag, tag.attrs):
            self.isResult = False
            self.results.append(self.info)
            return

        if self.isResult:
            if self.is_c_title(tag.tag, tag.attrs):
                self.isCTitle = False
                self.info.title = self.title_tmp
                self.title_tmp = ""
                return
            if self.is_c_title_author(tag.tag, tag.attrs):
                self.isAuthor = False
                return

    def handle_data(self,data):
        if self.isResult == False:
            return

        if self.isCTitle:
            self.title_tmp += data
            return
        if self.isAuthor and self.tags[-1].tag == 'div':
            if self.info.site == "":
                self.info.site = data
                return
            self.info.date = data
            return
         