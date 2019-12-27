# -*- coding: utf-8 -*-
import scrapy

from Luntan.items import KaoyanbangItem

import requests

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print(response.text)
            return response.text
        
    except ConnectionError:
        return None
list = []
page = 0
while page < 12:
    page = page + 1
    next_url = 'http://bbs.kaoyan.com/forum.php?mod=guide&view=hot&page=' + str(page)
    list.append(next_url)


class KaoyanbangSpider(scrapy.Spider):
    name = 'kaoyanbang'
    allowed_domains = ['bbs.kaoyan.com/']
    # # 随机选择一个代理
    # proxy = random.choice(proxy_list)
    start_urls = list

    def parse(self, response):
        items = response.xpath('//div[@id="threadlist"]/div[2]/table//tr')
        for post in items:
            item = KaoyanbangItem()
            item['posts_name'] = post.xpath('./th/a/text()').extract()
            item['posts_link'] = post.xpath('./th/a/@href').extract()
            item['poster_numbers'] = post.xpath('./th/span[1]/text()').extract()
            
            item['posts_section'] = post.xpath('./td[2]/a/text()').extract()
            item['posts_time'] = post.xpath('./td[3]//span/text()').extract()
            item['posts_replies'] = post.xpath('./td[4]/a/text()').extract()
            item['posts_pageview'] = post.xpath('./td[4]/em/text()').extract()
            item['poster'] = post.xpath('./td[3]//a/text()').extract()

            yield item

