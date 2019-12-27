import scrapy
import json
from News_education.items import ToutiaoItem
from urllib.parse import urlencode




def get_page_index(start_url,offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    url = start_url + urlencode(data)
    return url
class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['toutiao.com']
    keyword = "考研"
    offset = 0
    start_url = 'https://www.toutiao.com/api/search/content/?'
    url = get_page_index(start_url, offset, keyword)
    start_urls = [url]

    def parse(self, response):
        dic = json.loads(response.text)

        if dic and 'data' in dic.keys():
            for node in dic.get('data'):
                item = ToutiaoItem()
                try:
                    item['title'] = node.get("title")  # 标题
                    # print(item['title'])

                    item['intro'] = node.get("abstract")  # 简介
                    item['datetime'] = node.get("datetime")  # 发表时间
                    item['announcer'] = node.get("source")  # 来源
                    print(item['announcer'])
                    item["img"] = node.get("image_url")  # 图片
                    url = node.get("item_source_url")  # url
                    if url != None:
                        url = "https://www.toutiao.com" + url
                    else:
                        url = node.get("url")
                    item['url'] = url
                    # print(item['url'])

                    item['platform'] = "今日头条"  # 站内

                    # print(item)
                    yield item
                except:
                    pass
        if self.offset < 140:
            self.offset += 20
            url = get_page_index(self.start_url, self.offset, self.keyword)
            yield scrapy.Request(url, callback=self.parse)