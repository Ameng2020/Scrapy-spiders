# -*- coding: utf-8 -*-
import scrapy
from Luntan.items import Kaoyanbang_banItem
import re
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
# list = []
# page = 1
# while page < 3:
#     page = page + 1
#     next_url = 'http://bbs.kaoyan.com/f2107p' + str(page)
#     list.append(next_url)

class KaoyanbangBanSpider(scrapy.Spider):
    name = 'kaoyanbang_ban'
    allowed_domains = ['bbs.kaoyan.com']
    # start_urls = list
    start_urls =["http://bbs.kaoyan.com/"]

    def parse(self, response):

        li_list = response.xpath("//div[@id='category_173']/table/tr/td")

        for li in li_list:
            item = Kaoyanbang_banItem()
            item['posts_section'] = li.xpath("./dl/dt/a/text()").extract_first()
            item['posts_link'] = li.xpath('./dl/dt/a/@href').extract_first()
            print(item)
            yield scrapy.Request(item["posts_link"], callback=self.parse_detail, meta={"item": item})



    def parse_detail(self, response):
        # 处理详情页
        item = response.meta["item"]
        li_list = response.xpath("//table[@id='threadlisttableid']/tbody/tr")
        for li in li_list:
            link= li.xpath('./th/a[2]/@href').extract_first()
            if link is not "javascript:void(0);":
                item['posts_link_a'] = li.xpath('./th/a[2]/@href').extract_first()
                item['posts_name'] = li.xpath('./th/a[2]/text()').extract_first()
                item['posts_time'] = li.xpath("./td[@class='by']/em/span/text()").extract_first()
                item['posts_replies'] = li.xpath("./td[@class='num']/a/text()").extract_first()
                item['posts_pageview'] = li.xpath("./td[@class='num']/em/text()").extract_first()
                item['poster'] = li.xpath("./td[@class='by']/cite/a/text()").extract_first()
            # item["content"] = response.xpath("//div[@class='t_fsz']/table//tr/td/text()").extract()
            #
            # item["content_img"] = response.xpath("//ignore_js_op[@class='clearfix']/img/@src").extract()
            # print(item)
            yield item
        next_url = response.xpath("//div[@class='pg']/a[@class='nxt']/@href").extract_first()
        if next_url != None:
            yield scrapy.Request(next_url, callback=self.parse_detail, meta={"item": item})

