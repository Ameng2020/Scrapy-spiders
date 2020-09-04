# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


import random
from News_education.settings import USER_AGENTS
from .settings import PROXIES



# 随机的User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)

        request.headers.setdefault("User-Agent", useragent)


class RandomProxy(object):
    def  __init__(self, ip=''):
        self.ip = ip

    def  process_request(self,request,spider):
        thisip = random.choice(PROXIES)
        print("this is ip:" + thisip["ipaddr"])