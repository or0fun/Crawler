# -*- coding:utf-8 -*-

from crawler import Crawler
import xlwt#https://pypi.python.org/pypi/xlwt

import multiprocessing
import sys
import time
import os

def saveToFile(crawler, filename):
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = f.add_sheet('sheet 1')

    titles = ['日期', '网站名称', '文章标题', '阅读量', '评论数', '链接']

    for index in range(len(titles)):
        sheet.write(0, index, titles[index])

    row = 1

    tall_style = xlwt.easyxf('font:height 360;')

    sheet.row(0).set_style(tall_style)
    sheet.col(0).width = 6000
    sheet.col(2).width = 15000

    for result in crawler.realResults:
        sheet.write(row, 0, result.date)
        sheet.write(row, 1, result.site)
        sheet.write(row, 2, result.title)
        sheet.write(row, 3, result.behavior.views)
        sheet.write(row, 4, result.behavior.comments)
        sheet.write(row, 5, result.link)
        row = row + 1

    if os.path.exists("output") == False:
        os.makedirs('output')

    print filename
    f.save(filename)

def bdworker(words, fromdate):
    crawler = Crawler()

    bd_index = 0

    length = 0

    filename = "output/baidu_" + fromdate + "_" + words + "_" + time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())) + '.xls'
   
    while True:

        length = len(crawler.realResults)
        crawler.bdrun(words, fromdate, bd_index)
        if False == crawler.bd_result:
            break
        if len(crawler.realResults) == length:
            break
        bd_index += 20

    print len(crawler.realResults)
    
    saveToFile(crawler, filename)

def gworker(words, fromdate):
    crawler = Crawler()

    bd_index = 0

    length = 0

    filename = "output/google_" + fromdate + "_" + words + "_" + time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())) + '.xls'
   
    while True:

        length = len(crawler.realResults)
        crawler.grun(words, fromdate, bd_index)
        if False == crawler.bd_result:
            break
        break

    print len(crawler.realResults)
    
    saveToFile(crawler, filename)

    

if __name__ == "__main__":

    words = sys.argv[1]
    fromdate = sys.argv[2]
    # p = multiprocessing.Process(target = bdworker, args = (words,fromdate,))
    # p.start()
    # print "p.pid:", p.pid
    # print "p.name:", p.name
    # print "p.is_alive:", p.is_alive()

    p2 = multiprocessing.Process(target = gworker, args = (words,fromdate,))
    p2.start()
    print "p2.pid:", p2.pid
    print "p2.name:", p2.name
    print "p2.is_alive:", p2.is_alive()
