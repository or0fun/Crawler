# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

import bd
from bd import BdResultsParser

import time

startTime = time.time()

words = 'YunOS'
index = 0

url = 'http://news.baidu.com/ns?word=title%3A%28'+ str(words) + '%29&pn=' + str(index) + '&cl=2&ct=1&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0'
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = { 'User-Agent' : user_agent }

print url
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    print time.time() - startTime

    content = response.read()

    print time.time() - startTime

    parser = BdResultsParser()
    parser.feed(content)

    print len(parser.results)

    for result in parser.results:
        print result.title
        print result.site
        print result.date
        print result.link
        print result.children
        pass

    print time.time() - startTime

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason