# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .import settings
from Luntan.items import KaoyanbangItem,Kaoyanbang_banItem



class LuntanPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        if item.__class__ == Kaoyanbang_banItem:
            # posts_name = item['posts_name']
            # posts_link = item['posts_link']
            # posts_link_a = item['posts_link_a']
            # posts_time = item['posts_time']
            #
            # posts_section = item['posts_section']
            # posts_replies = item['posts_replies']
            # posts_pageview = item['posts_pageview']
            # poster = item['poster']

            posts_name = "".join(item['posts_name'])
            posts_link = "".join(item['posts_link'])
            posts_link_a = "".join(item['posts_link_a'])
            posts_time = "".join(item['posts_time'])

            posts_section = "".join(item['posts_section'])
            posts_replies = "".join(item['posts_replies'])
            posts_pageview = "".join(item['posts_pageview'])
            poster = "".join(item['poster'])

            # self.cursor.execute(
            #     """insert into forum_kaoyanbang(posts_name,posts_link,posts_link_a,posts_time,posts_section,posts_replies,posts_pageview,poster)
            #       value (%s,%s,%s,%s,%s,%s,%s,%s)""",
            #     (posts_name,
            #      posts_link,
            #      posts_link_a,
            #      posts_time,
            #      posts_section,
            #      posts_replies,
            #      posts_pageview,
            #      poster,
            #
            #      ))
            # self.connect.commit()
            # return item
            try:
                self.cursor.execute("""select * from forum_kaoyanbang where posts_link_a = %s""", posts_link_a)
                ret = self.cursor.fetchone()
                if ret:
                    self.cursor.execute(
                        """update forum_kaoyanbang set posts_name = %s,posts_link = %s,posts_link_a = %s,posts_time = %s,
                            posts_section = %s,posts_replies = %s,posts_pageview = %s,poster =%s
                            where posts_link_a  = %s""",
                        (posts_name,
                         posts_link,
                         posts_link_a,
                         posts_time,

                         posts_section,
                         posts_replies,
                         posts_pageview,
                         poster,
                         posts_link_a,
                         ))
                else:
                    self.cursor.execute(
                        """insert into forum_kaoyanbang(posts_name,posts_link,posts_link_a,posts_time,posts_section,posts_replies,posts_pageview,poster)
                          value (%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (posts_name,
                         posts_link,
                         posts_link_a,
                         posts_time,
                         posts_section,
                         posts_replies,
                         posts_pageview,
                         poster,

                         ))
                self.connect.commit()
            except Exception as error:
                print("错误")
            return item




        elif item.__class__ == KaoyanbangItem:

            posts_name = "".join(item['posts_name'])
            posts_link = "".join(item['posts_link'])
            posts_time = "".join(item['posts_time'])
            poster_numbers = "".join(item['poster_numbers'])
            posts_section = "".join(item['posts_section'])
            posts_replies = "".join(item['posts_replies'])
            posts_pageview = "".join(item['posts_pageview'])
            poster = "".join(item['poster'])
            try:
                self.cursor.execute("""select * from forum_kaoyanbang_hot where posts_link = %s""", posts_link)
                ret = self.cursor.fetchone()
                if ret:
                    self.cursor.execute(
                        """update forum_kaoyanbang_hot set posts_name = %s,posts_link = %s,posts_time = %s,
                            poster_numbers = %s,posts_section = %s,posts_replies = %s,posts_pageview = %s,poster =%s
                            where posts_link  = %s""",
                        (posts_name,
                         posts_link,
                         posts_time,
                         poster_numbers,
                         posts_section,
                         posts_replies,
                         posts_pageview,
                         poster,
                         posts_link,
                         ))
                else:
                    self.cursor.execute(
                        """insert into forum_kaoyanbang_hot(posts_name,posts_link,posts_time,poster_numbers,posts_section,posts_replies,posts_pageview,poster)
                          value (%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (posts_name,
                         posts_link,
                         posts_time,
                         poster_numbers,
                         posts_section,
                         posts_replies,
                         posts_pageview,
                         poster,

                         ))
                self.connect.commit()
            except Exception as error:
                print("错误")
            return item

    def close_spider(self, spider):  # 该方法在spider被关闭的时候打开，我们可以在这里做一些收尾工作，
        self.connect.close()  # 例如：关闭数据库


