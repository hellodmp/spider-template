#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
需要密码登录的爬虫模板
'''
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from template.items import ZhihuItem

class ZhihuSipder(CrawlSpider) :
    name = "wordpress"
    start_urls = [
        "http://121.42.223.111/"
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow = ('/question/\d+#.*?', )), callback = 'parse_page', follow = True),
        Rule(SgmlLinkExtractor(allow = ('/question/\d+', )), callback = 'parse_page', follow = True),
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:27.0) Gecko/20100101 Firefox/27.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept': 'Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept': 'Encoding: gzip, deflate',
    }

    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("http://121.42.223.111/wp-login.php", meta = {'cookiejar' : 1}, callback = self.post_login)]

    #FormRequeset出问题了
    def post_login(self, response):
        print 'Preparing login'

        return [FormRequest.from_response(response,
                            meta = {'cookiejar' : response.meta['cookiejar']},
                            headers = self.headers,  #注意此处的headers
                            formdata = {
                            'log': 'admin',
                            'pwd': 'lngwordpress',
                            'wp-submit': '登录',
                            'redirect_to': 'http://121.42.223.111/wp-admin/index.php',
                            'testcookie': '1'
                            },
                            callback = self.after_login,
                            dont_filter = True
                            )]

    def after_login(self, response) :
        #print response.body
        file = open('test1.html','w')
        file.write(response.body)
        file.close()
        '''
        for url in self.start_urls :
            yield self.make_requests_from_url(url)
        '''

    def parse_page(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        return item