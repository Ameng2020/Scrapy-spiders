# -*- coding: utf-8 -*-

# Scrapy settings for Luntan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Luntan'

SPIDER_MODULES = ['Luntan.spiders']
NEWSPIDER_MODULE = 'Luntan.spiders'

MYSQL_HOST = '192.168.1.100'
MYSQL_DBNAME = 'kaoyan'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'

LOG_LEVE = "WARNING"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Luntan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COMMANDS_MODULE = 'Luntan.commands'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Luntan.middlewares.LuntanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {

   'Luntan.middlewares.RandomUserAgent': 1,
    # 'Luntan.middlewares.RandomProxy': 100
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Luntan.pipelines.LuntanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]
# PROXIES = [
#     {'ipaddr': '111.8.60.9:8123' },
#     {"ipaddr": "182.47.86.249:8118"},
#     {"ipaddr": "114.119.116.92:61066"},
#     {"ipaddr": "171.83.166.97:9999"},
#     {"ipaddr": "117.114.149.66:53281"},
#     {"ipaddr": "42.123.125.181:8088"},
#     {"ipaddr": "112.85.170.182:9999"},
#     {"ipaddr": "211.152.33.24:48749"},
#     {"ipaddr": "112.85.170.208:9999"},
#     {"ipaddr": "112.85.168.174:9999"},
#     {"ipaddr": "112.85.168.228:9999"},
#     {"ipaddr": "110.52.235.136:9999"},
#     {"ipaddr": "183.148.129.120:9999"},
#     {"ipaddr": "112.85.128.66:9999"},
# {"ipaddr": "122.235.242.116:8118"},
# {"ipaddr": "119.179.135.244:8060"},
# {"ipaddr": "14.29.232.142:8082"},
# {"ipaddr": "116.209.55.230:9999"},
# {"ipaddr": "116.209.59.162:9999"},
# {"ipaddr": "101.132.161.82:8080"},
# {"ipaddr": "138.204.23.110:53281"},
# {"ipaddr": "123.188.91.28:80"},
# {"ipaddr": "220.198.127.183:80"},
# {"ipaddr": "197.234.55.217:8083"},
# {"ipaddr": "171.83.166.197:9999"},
# 
# ]