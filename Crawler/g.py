#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from tag import Tag
from tag import Info

from HTMLParser import HTMLParser

class GResultsParser(HTMLParser):

    def __init__(self, baseInfo):   
        HTMLParser.__init__(self) 

        self.baseInfo = baseInfo
        self.results = []
        self.isResult = False
        self.isCTitle = False
        self.isAuthor = False
        self.isDate = False
        self.tags = []

        self.info = Info()
        self.title_tmp = ""

        self.lastTag = ""

    def is_result_title(self,tag,attrs):
        if tag == 'div' and attrs:
            for key, value in attrs:
                if key == 'class' and value == '_cnc':
                    return True
        return False

    def is_c_title(self,tag,attrs):
        if False == self.isResult:
            return False
        if tag == 'h3' and attrs:
            for key, value in attrs:
                if key == 'class' and value == 'r _U6c':
                    return True
        return False

    def is_c_title_author(self,tag,attrs):
        if False == self.isResult:
            return False
        if tag == 'span' and attrs:
            for key, value in attrs:
                if key == 'class' and value == '_tQb _IId':
                    return True
        return False

    def is_date(self,tag,attrs):
        if False == self.isResult:
            return False
        if tag == 'span' and attrs:
            for key, value in attrs:
                if key == 'class' and value == 'f nsa _uQb':
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
                    self.info.link = "https://www.google.com" + value
                    return

        if self.is_c_title_author(tag, attrs):
            self.isAuthor = True
            return

        if self.is_date(tag, attrs):
            self.isDate = True
            return

    def handle_endtag(self,tag):

        if self.isResult == False:
            return

        tag = self.tags.pop()
        if self.is_result_title(tag.tag, tag.attrs):
            self.isResult = False
            if None == self.baseInfo:
                self.results.append(self.info)
            else:
                if self.baseInfo.title == self.info.title and self.baseInfo.date == self.info.date and self.baseInfo.site == self.info.site:
                    return
                else:
                    self.results.append(self.info)

        if self.isResult:
            if self.is_c_title(tag.tag, tag.attrs):
                self.isCTitle = False
                self.info.title = self.title_tmp
                self.title_tmp = ""
                return
            if self.is_c_title_author(tag.tag, tag.attrs):
                self.isAuthor = False
                return
            if self.is_date(tag.tag, tag.attrs):
                self.isDate = False
                return

    def handle_data(self,data):
        if len(data) < 100:
            print data
            pass
        if self.isResult == False:
            return

        print data
        if self.isCTitle:
            self.title_tmp += data
            return
        if self.isAuthor:
            self.info.site = data
            return
        if self.isDate:
            self.info.date = data
            return
         