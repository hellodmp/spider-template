#-*- coding: utf-8 -*-

import urllib, urllib2, cookielib

# 构造requests header, 照抄就行
#参考http://www.devlabs.cn/?p=240
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:27.0) Gecko/20100101 Firefox/27.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept': 'Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept': 'Encoding: gzip, deflate',
}

# 要提交的数据
postdata = {
    'log': 'admin',
    'pwd': 'lngwordpress',
    'wp-submit': '登录',
    'redirect_to': 'http://121.42.223.111/wp-admin/index.php',
    'testcookie': '1'
}

# 登录页面地址
url = 'http://121.42.223.111/wp-login.php'

cookie = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)

#请求页面()
req =urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req).read()

# 登录, 提交数据
postdata = urllib.urlencode(postdata)
#组装请求
req = urllib2.Request(
    url = url,
    data = postdata,
    headers = headers
    )
req = urllib2.Request(url, headers=headers, data=postdata)
res = urllib2.urlopen(req).read()

file = open('test.html','w')
file.write(res)
file.close()
