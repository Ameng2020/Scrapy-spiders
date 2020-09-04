# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from News_education.items import NewsEducationItem
import requests

class BaiduSpider(CrawlSpider):

    name = 'baidu'
    # allowed_domains = ['baidu.com']
    # start_urls = ['https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E8%80%83%E7%A0%94']

    def __init__(self, q=None, *args, **kwargs):
        super(BaiduSpider, self).__init__(*args, **kwargs)
        # 定义要爬取的页数, 这里设置两页，可以演示功能
        self.pagenums = 2
        self.queryword = q

        self.start_urls = ['https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd={}&pn=0'.format(self.queryword)]



    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='result']/h3/a")), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']")), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//div[@class='article-title']/h2/text()").extract_first()
        item['author'] = response.xpath("//div[@class='author-txt']/p/text()").extract_first()
        item['time'] = response.xpath("//div[@class='author-txt']/div/span/text()").extract()
        item['content'] = response.xpath("//div[@class='article-content']/p/text()").extract()
        item['img'] = response.xpath("//div[@class='article-content']/div[@class='img-container']/img/src").extract()
        print(item)
        return item
