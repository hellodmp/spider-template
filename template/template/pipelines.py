# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#JsonPipeline需要的包
import json
import codecs
from collections import OrderedDict

#MySQLStorePipeline所需的包
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi #导入twisted的包


class TemplatePipeline(object):
    def process_item(self, item, spider):
        return item

#将item保存以json的格式保存到文件中
class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('D://data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


#将Item保存到MySql数据库表中
class MySQLStorePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'wordpress',
                user = 'root',
                passwd = 'lng2015mysql',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        #query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        #插入数据库
        dict = {'chinalng':2, 'china5e':3, 'chinagas':4, 'lngche':5, 'mylng':6, 'gasonline':7, 'yeslng':8, 'weixin':9, 'baidu':10}
        category = 0
        if item['name'] in dict.keys():
            category = dict[item['name']]
        sql = "insert into wp_term_relationships (object_id, term_taxonomy_id) values (%d, %d)"%(id, category)
        tx.execute(sql)
