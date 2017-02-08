# -*- coding:utf-8 -*-

from crawler import Crawler


crawler = Crawler()

bd_index = 0

while True:
    crawler.bdrun('YunOS', bd_index)
    if False == crawler.bd_result:
        break
    bd_index += 20
    break

print crawler.bd_total_count
print len(crawler.realResults)