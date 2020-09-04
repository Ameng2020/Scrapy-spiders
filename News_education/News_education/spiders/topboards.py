# -*- coding: utf-8 -*-
import scrapy
from News_education.items import TopboardsItem

class TopboardsSpider(scrapy.Spider):
    name = 'topboards'
    allowed_domains = ['http://top.baidu.com']
    start_urls = ['http://top.baidu.com/buzz?b=12&fr=topboards']
    #百度风云榜

    def parse(self, response):
        list = response.xpath("//div[@class='grayborder']/table/tr")
        for li in list:
            item = TopboardsItem()
            item['top'] = li.xpath("./td[@class='first']/span/text()").extract_first()
            item['school'] = li.xpath("./td[@class='keyword']/a/text()").extract_first()
            item['url'] = li.xpath("./td[@class='keyword']/a/@href").extract_first()
            item['jianjie_url'] = li.xpath("./td[@class='tc']/a[1]/@href").extract_first()
            item['new_url'] = li.xpath("./td[@class='tc']/a[2]/@href").extract_first()
            item['v_url'] = li.xpath("./td[@class='tc']/a[3]/@href").extract_first()
            item['search'] = li.xpath("./td[@class='last']/span/text()").extract_first()
            item['search_vary'] = li.xpath("./td[@class='last']/span/@class").extract_first()
            yield item





