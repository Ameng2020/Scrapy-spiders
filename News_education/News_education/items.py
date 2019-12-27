# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsEducationItem(scrapy.Item):
    new_id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    intro = scrapy.Field()
    img = scrapy.Field()
    kl = scrapy.Field()
    time = scrapy.Field()
    media = scrapy.Field()
    source = scrapy.Field()
    crawled = scrapy.Field()

class TopboardsItem(scrapy.Item):
    top= scrapy.Field()
    school= scrapy.Field()
    url= scrapy.Field()
    jianjie_url= scrapy.Field()
    new_url= scrapy.Field()
    v_url= scrapy.Field()
    search= scrapy.Field()  #搜索指数
    search_vary= scrapy.Field()  #排行变化 icon-fair=不变  icon-fall=下降  icon-rise=上升
    crawled = scrapy.Field()


class ToutiaoItem(scrapy.Item):
    title = scrapy.Field()

    platform = scrapy.Field()
    url = scrapy.Field()
    # content = scrapy.Field()
    datetime = scrapy.Field()
    announcer = scrapy.Field()
    crawled = scrapy.Field()
    intro = scrapy.Field()
    img = scrapy.Field()
