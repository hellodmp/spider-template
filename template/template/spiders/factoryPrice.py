# -*- coding:utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.http.request import Request
from scrapy.selector import Selector
from lngPrice.items import FactoryItem
import MySQLdb
import datetime


class factoryPriceSpider(BaseSpider):

    name = "factoryPrice"
    start_urls = ["http://market.yeslng.com/"]

    def parse(self, response):
        sel = Selector(response)
        list = sel.xpath('//tr[@class="top-2"]')
        #list = sel.xpath('//tr[contains(@class,"top")]')

        item_list= []
        for tr in list:
            item = FactoryItem()
            name = tr.xpath('td[@class="lng-name"]/a/text()').extract()[0].strip()
            price = tr.xpath('td[@class="today-price"]/span/text()').extract()[0].strip()
            time = tr.xpath('td[@class="adjust-price"]/span/text()').extract()[0].strip()
            if time != u"最新":
                continue
            item['name'] = name
            item['price'] = int(price)
            item_list.append(item)
            print item
        self.Insert(item_list)

    def Insert(self, list):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='lng2015mysql',db='lng_price',port=3306,charset='utf8')
            cur=conn.cursor()
            timeStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            template = "insert into factory_price (factory_name,price,date) values ('%s', %d, '%s')"
            for item in list:
                print item['name'], item['price'], timeStr
                sql = template%(item['name'], item['price'], timeStr)
                print sql
                cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
             print "Mysql Error %d: %s" % (e.args[0], e.args[1])

