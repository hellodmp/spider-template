# -*- coding:utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.http.request import Request
from scrapy.selector import Selector
from template.items import NewsItem
import re

#爬取微信搜索得到的公众号结果
class weixinSpider(BaseSpider):
    name = "weixin"
    #初始化多个url
    start_urls = ["http://weixin.sogou.com/weixin?query=lng&fr=sgsearch&tsn=1&interation=&type=2&page="+str(i)+"&ie=utf8" for i in range(1,5)]

    def item_parse(self, response):
        print response.meta['url']
        return

    def parse(self, response):
        sel = Selector(response)
        urls = sel.xpath('//div[@class="img_box2"]/a[@target]/@href').extract()
        for item_url in urls:
            yield Request(item_url, meta={'url':item_url },callback=self.item_parse)


