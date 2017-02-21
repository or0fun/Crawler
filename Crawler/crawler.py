#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib
import urllib2
import re

import bd
from bd import BdResultsParser
from g import GResultsParser
from tag import Behavior

import time

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Crawler(object):

	def __init__(self):  

		self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
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
		    if content.find('<meta charset="gbk"') > -1:
		    	content = content.decode('gbk')
		    elif content.find('<meta charset="UTF-8"') > -1:
		    	content = content.decode('UTF-8')
		    elif content.find('<meta charset="gb2312"') > -1:
		    	content = content.decode('gb2312')
		    else:
		    	content = content.decode('utf-8')
		    return content
		except urllib2.URLError, e:
		    if hasattr(e,"code"):
		        print e.code
		    if hasattr(e,"reason"):
		        print e.reason
		    print e
		return ""

	def bd_crawler(self, url, baseInfo):

	    content = self.request_content(url)
	    parser = BdResultsParser(baseInfo)
	    parser.feed(content)

	    for result in parser.results:
	        if self.is_time_valid(self.fromdate, result.date):
	        	self.realResults.append(result)
	        	self.bd_result = True
	        else:
	        	self.bd_result = False

	        if result.children.find('http') > -1:
	        	self.bd_crawler(result.children, result)

	def g_crawler(self, url, baseInfo):
	    content = self.request_content(url)
	    content = content.replace('</g;Aa=/>','')
	    
	    parser = GResultsParser(baseInfo)
	    parser.feed(content.encode("utf-8"))

	    for result in parser.results:
	        if self.is_time_valid(self.fromdate, result.date):
	        	self.realResults.append(result)
	        	self.bd_result = True
	        else:
	        	self.bd_result = False

	        if result.children.find('http') > -1:
	        	self.g_crawler(result.children, result)
	       
	def grun(self, words, fromdate, index):

		self.fromdate = fromdate
		words = words.replace(' ', '+')

		url = 'http://www.google.com/search?q='+ str(words) + '&hl=en&gl=us&authuser=0&tbm=nws&start=' + str(index)

		self.g_crawler(url, None)

	def bdrun(self, words, fromdate, index):

		self.fromdate = fromdate
		words = words.replace(' ', '+')

		url = 'http://news.baidu.com/ns?word='+ str(words) + '&rn=20&tn=news&clk=sortbytime&pn=' + str(index)

		self.bd_crawler(url, None)

		for result in self.realResults:
			if result.link.find('hexun.com') > -1:
				behavior = self.hexun(result.link)
				result.bevavior = behavior

			if result.link.find('zol.com') > -1:
				behavior = self.zol(result.link)
				result.bevavior = behavior

			if result.link.find('ifeng.com') > -1:
				behavior = self.ifeng(result.link)
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

	def ifeng(self, url):
 
		searchObj = re.search( r'/([-a-z0-9]+)\.shtml', url, re.M|re.I)
		if searchObj:
			comment_url = "http://survey.news.ifeng.com/getaccumulator_weight.php?format=js&serverid=2&key=" + searchObj.group(1) + "&callback=f15a288854f41"

			content = self.request_content(comment_url)
    		
			searchObj = re.search( r'"browse":([0-9]+)}', content, re.M|re.I)
			if searchObj:
				return Behavior(0, searchObj.group(1))

		return Behavior(0, 0)

	def is_time_valid(self, frome_date, news_date):
		from_time = time.mktime(time.strptime(frome_date,'%Y-%m-%d')) # get the seconds for specify date
		if news_date.find(u'年') == -1:
			return True
		space_index = news_date.find(' ')
		news_date = news_date[0:space_index]
		news_time = time.mktime(time.strptime(news_date,u'%Y年%m月%d日'))
		if (float(news_time) >= float(from_time)):
			return True
		return False

	def prn_obj(self, obj):
		print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])

