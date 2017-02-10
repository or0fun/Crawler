#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib
import urllib2
import re

import bd
from bd import BdResultsParser
from tag import Behavior

import time


class Crawler(object):

	def __init__(self):  

		self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
		self.headers = { 'User-Agent' : self.user_agent }

		self.bd_result = True
		self.realResults = []
		self.bd_total_count = 0

		self.fromdate = ""

	def request_content(self, url):
		try:
		    request = urllib2.Request(url, headers = self.headers)
		    response = urllib2.urlopen(request)
		    content = response.read()
		    return content
		except urllib2.URLError, e:
		    if hasattr(e,"code"):
		        print e.code
		    if hasattr(e,"reason"):
		        print e.reason
		return ""

	def bd_crawler(self, url):

	    content = self.request_content(url)
	    parser = BdResultsParser()
	    parser.feed(content)

	    length = len(parser.results)

	    self.bd_total_count += length

	    for result in parser.results:
	        if result.children.find('http') > -1:
	        	self.bd_crawler(result.children)
	        else:
	        	if self.is_time_valid(self.fromdate, result.date):
	        		self.realResults.append(result)
	        		self.bd_result = True
	        	else:
	        		self.bd_result = False

	    if length < 20:
	    	self.bd_result = False

	def bdrun(self, words, fromdate, index):

		self.fromdate = fromdate
		words = words.replace(' ', '+')

		url = 'http://news.baidu.com/ns?word=title%3A%28'+ str(words) + '%29&pn=' + str(index) + '&cl=2&ct=1&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0&clk=sortbytime'
		
		self.bd_crawler(url)

		for result in self.realResults:
			if result.link.find('hexun.com') > -1:
				behavior = self.hexun(result.link)
				result.bevavior = behavior

			if result.link.find('zol.com') > -1:
				behavior = self.zol(result.link)
				result.bevavior = behavior

	def hexun(self, url):
 
		searchObj = re.search( r'/([0-9]+)\.html', url, re.M|re.I)
		if searchObj:
			comment_url = 'http://comment.tool.hexun.com/Comment/GetComment.do?commentsource=3&articleid=' + searchObj.group(1) + '&articlesource=1&pagenum=1&pagesize=3&callback=hexunapi_04351924806556662'

			content = self.request_content(comment_url)
    		
			searchObj = re.search( r'"commentcount":([0-9]+),', content, re.M|re.I)
			if searchObj:
				return Behavior(searchObj.group(1), 0)

		return Behavior(0, 0)

	def zol(self, url):

		content = self.request_content(url)
		searchObj = re.search( r'"<em class="comment-num">([0-9]+)</em>', content, re.M|re.I)
		if searchObj:
			return Behavior(searchObj.group(1), 0)

		return Behavior(0, 0)

	def is_time_valid(self, frome_date, news_date):
		from_time = time.mktime(time.strptime(frome_date,'%Y-%m-%d')) # get the seconds for specify date
		if news_date.find('年') == -1:
			return True
		space_index = news_date.find(' ')
		news_date = news_date[0:space_index]
		news_time = time.mktime(time.strptime(news_date,'%Y年%m月%d日'))
		if (float(news_time) >= float(from_time)):
			return True
		return False



