# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

import bd
from bd import BdResultsParser


words = 'YunOS'
index = 0
url = 'http://news.baidu.com/ns?word=title%3A%28'+ str(words) + '%29&pn=' + str(index) + '&cl=2&ct=1&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    parser = BdResultsParser()
    parser.feed(content)
    for result in parser.results:
        print result.title
        pass

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason