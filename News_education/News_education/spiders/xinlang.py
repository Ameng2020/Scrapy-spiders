# -*- coding: utf-8 -*-
import scrapy
import json

from News_education.items import NewsEducationItem
from urllib.parse import urlencode
from selenium import webdriver

def get_page_index(start_url,page, q):
    data = {
        'q': q,
        'range': 'title',
        'c': 'news',
        'sort': 'time',
        'ie':'utf-8',
        'form': 'dfz_api',
        'page': page,

    }
    url = start_url + urlencode(data)
    return url



class XinlangSpider(scrapy.Spider):
    name = 'xinlang'
    # allowed_domains = ['sina.com.cn']

    # start_urls = ['http://api.search.sina.com.cn/?q=%E8%80%83%E7%A0%94&range=title&c=news&sort=time&ie=utf-8&from=dfz_api&callback=jsonp1557648836969']
    q = "考研"
    page = 1
    start_url = 'http://api.search.sina.com.cn/?'
    url = get_page_index(start_url, page, q)
    start_urls = [url]



    def parse(self, response):

        result = json.loads(response.text)

        page= result['result']['page']
        page = int(page)

        list = result['result']['list']
        # str(list).decode('utf-8')
        print(list)
        for li in list:
            item = NewsEducationItem()
            # item ={}
            item["new_id"] = li['id']
            item["title"] = li['title']
            item["url"] = li['url']
            item["intro"] = li['intro']
            item["img"] = li['imgurl']
            item["kl"] = li['kl']
            item["time"] = li['datetime']
            item["media"] = li['media']
            item["source"] = '新浪'
            # print(item)
            yield item
        # if list != None:
        #     next_url = 'http://api.search.sina.com.cn/?q=%E8%80%83%E7%A0%94&range=title&c=news&sort=time&ie=utf-8&from=dfz_api&callback=jsonp1557304899273&page='+page
        #
        #     yield scrapy.Request(url=next_url,callback=self.parse)
        if page < 9:
            self.page = str(page +1)
            url = get_page_index(self.start_url, self.page, self.q)
            yield scrapy.Request(url, callback=self.parse)







