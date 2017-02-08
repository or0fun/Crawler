

import urllib
import urllib2
import re

import bd
from bd import BdResultsParser

import time


class Crawler(object):

	def __init__(self):  

		self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
		self.headers = { 'User-Agent' : self.user_agent }

		self.bd_result = True
		self.realResults = []
		self.bd_total_count = 0

	def bd_crawler(self, url):

		startTime = time.time()

		try:
		    request = urllib2.Request(url,headers = self.headers)
		    response = urllib2.urlopen(request)
		    print time.time() - startTime

		    content = response.read()

		    print time.time() - startTime

		    parser = BdResultsParser()
		    parser.feed(content)

		    length = len(parser.results)

		    self.bd_total_count += length
		    print length
		    if length < 20:
		    	bd_result = False

		    for result in parser.results:
		        print result.title
		        print result.site
		        print result.date
		        print result.link
		        print result.children
		        if result.children.find('http') > -1:
		        	self.bd_crawler(result.children)
		        else:
		        	self.realResults.append(result)
		    
		    print time.time() - startTime

		except urllib2.URLError, e:
		    if hasattr(e,"code"):
		        print e.code
		    if hasattr(e,"reason"):
		        print e.reason

	def bdrun(self, words, index):

		url = 'http://news.baidu.com/ns?word=title%3A%28'+ str(words) + '%29&pn=' + str(index) + '&cl=2&ct=1&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0'
		
		self.bd_crawler(url)
