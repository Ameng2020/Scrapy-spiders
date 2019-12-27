# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KaoyanbangItem(scrapy.Item):
    posts_name = scrapy.Field()  # 标题名
    posts_time = scrapy.Field()
    link_a = scrapy.Field()  # 不完整的链接
    posts_link = scrapy.Field()  # 链接
    poster_numbers = scrapy.Field()  # 帖子参与数量
    posts_section = scrapy.Field()  # 帖子版块
    posts_replies = scrapy.Field()  # 帖子回复人数
    posts_pageview = scrapy.Field()  # 帖子阅读人数
    poster = scrapy.Field()  # 帖子作者
    pass


class Kaoyanbang_banItem(scrapy.Item):

    posts_name = scrapy.Field()  # 标题名
    posts_link_a = scrapy.Field()  #不完整的链接
    posts_time = scrapy.Field()
    posts_link = scrapy.Field()  # 链接

    posts_section = scrapy.Field() #帖子版块
    posts_replies = scrapy.Field()  #帖子回复人数
    posts_pageview = scrapy.Field() #帖子阅读人数
    poster = scrapy.Field()     #帖子作者
    # content_img =scrapy.Field()
    # content = scrapy.Field()
    pass
