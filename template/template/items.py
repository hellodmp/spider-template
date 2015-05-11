# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TemplateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#新闻需要保存的字段
class NewsItem(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()

class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()  #保存抓取问题的url
    title = scrapy.Field()  #抓取问题的标题
    description = scrapy.Field()  #抓取问题的描述
    answer = scrapy.Field()  #抓取问题的答案
    name = scrapy.Field()  #个人用户的名称
