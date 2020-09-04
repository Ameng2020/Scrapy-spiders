# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import pymysql
from .import settings
from News_education.items import NewsEducationItem,TopboardsItem,ToutiaoItem



class NewsEducationPipeline(object):
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
        item["crawled"] = datetime.now()
        if item.__class__ == NewsEducationItem:

            crawled = item["crawled"]
            new_id = item["new_id"]
            title  = item["title"]
            url = item["url"]
            intro = item["intro"]
            img = item["img"]
            kl = item["kl"]
            time = item["time"]
            media = item["media"]
            source = item["source"]

            try:
                self.cursor.execute("""select * from new_info where url = %s""", url)
                ret = self.cursor.fetchone()
                if ret:
                    self.cursor.execute(
                        """update new_info set new_id = %s,title = %s,intro = %s,img = %s,
                            url = %s,kl = %s,time = %s,crawled =%s,media =%s,source =%s
                            where url  = %s""",
                        (new_id,
                         title,
                         intro,
                         img,
                         url,
                         kl,
                         time,
                         crawled,
                         media,
                         source,
                         url,
                         ))
                else:
                    self.cursor.execute(
                        """insert into new_info(new_id,title,intro,img,url,kl,time,crawled, media,source)
                          value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (new_id,
                         title,
                         intro,
                         img,
                         url,
                         kl,
                         time,
                         crawled,
                         media,
                         source,

                         ))
                    self.connect.commit()


            except Exception as error:
                print("错误")
            return item


        elif item.__class__ == TopboardsItem:
            crawled = item["crawled"]
            top = item["top"]
            school = item["school"]
            url = item["url"]
            jianjie_url = item["jianjie_url"]
            new_url = item["new_url"]
            v_url = item["v_url"]
            search = item["search"]
            search_vary = item["search_vary"]
            try:
                self.cursor.execute("""select * from topboards where school = %s""",school)
                ret = self.cursor.fetchone()
                if ret:
                    self.cursor.execute(
                        """update topboards set top = %s,crawled =%s,search =%s,search_vary =%s
                            where school  = %s""",
                        (top,

                         crawled,
                         search,
                         search_vary,
                         school,
                         ))
                else:
                    self.cursor.execute(
                        """insert into topboards(top,school,url,jianjie_url,new_url,v_url,search,crawled,search_vary)
                          value (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (top,
                         school,
                         url,
                         jianjie_url,
                         new_url,
                         v_url,
                         search,
                         crawled,
                         search_vary

                         ))
                    self.connect.commit()


            except Exception as error:
                print("错误")
            return item

        elif item.__class__ == ToutiaoItem:
            crawled = item["crawled"]
            if item['title'] != None:
                title = item['title']

                time = item['datetime']
                announcer = item['announcer']
                url = item['url']
                platform = item['platform']
                intro = item['intro']
                img = item['img']
                # content =item['content']
                try:
                    self.cursor.execute("""select * from toutiao where url = %s""", url)
                    ret = self.cursor.fetchone()
                    if ret:
                        self.cursor.execute(
                            """update toutiao set title = %s,url =%s,time =%s,announcer=%s,platform=%s,crawled=%s,intro=%s,img=%s
                                where url  = %s""",
                            (title,
                             url,
                             time,
                             announcer,
                             platform,
                             crawled,
                             intro,
                             img,
                             url
                             ))
                    else:
                        self.cursor.execute(
                            """insert into toutiao(title,url,time,announcer,platform,crawled,intro,img)
                              value (%s,%s,%s,%s,%s,%s,%s,%s)""",
                            (title,
                             url,
                             time,
                             announcer,
                             platform,
                             crawled,
                             intro,
                             img,

                             ))
                        self.connect.commit()


                except Exception as error:
                    print("错误")
                return item





