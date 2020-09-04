# -*- coding: utf-8 -*-
import scrapy
from News_education.items import NewsEducationItem
import re
import urllib.request
from lxml import etree
from selenium import webdriver
from time import sleep

class NewsBaiduSpider(scrapy.Spider):
    name = 'news_baidu'
    # allowed_domains = ['https://www.baidu.com/s?tn=news']
    # start_urls = ['https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E8%80%83%E7%A0%94']
    def __init__(self, q='考研', *args, **kwargs):
        super(NewsBaiduSpider, self).__init__(*args, **kwargs)
        # 定义要爬取的页数, 这里设置两页，可以演示功能
        # self.pagenums = 2
        self.queryword = q

        self.start_urls = ['https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd={}&pn=0'.format(self.queryword)]

    def parse(self, response):

        print(response.text)
        node_list = response.xpath("//div[@class='result']")
        for li in node_list:
            item = NewsEducationItem()
            item['url'] = li.xpath('./h3/a/@href').extract_first()
            item['title'] = li.xpath('./h3/a/text()')
            item['text'] = li.xpath("./div/p[@class='c-author']/text()")
            # item['author']=
            # item['time']=
            print(item)
            # yield item

        next_url = response.xpath('//p[@id="page"]/a[10]/@href').extract_first()

        if next_url is not None:
            next_url= 'https://www.baidu.com'+next_url
            yield scrapy.Request(next_url, callback=self.parse)






