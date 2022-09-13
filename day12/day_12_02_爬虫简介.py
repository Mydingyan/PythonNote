# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_12_02_爬虫简介.py
@time: 2022/9/13 22:31
"""


# 爬虫
'''

流程: 获取数据--解析提取数据--存储

需要了解计算机网络知识,Python基础

提取html中数据的方法:
BeautifulSoup,正则,XPath,CSS Selector

存储数据:
文本,CSV , 数据库  
'''

import requests
from lxml import html #可以解析HTMT页面的库
from requests.packages.urllib3.exceptions import InsecureRequestWarning   #忽略不安全请求警告?
# 下载壁纸爬虫

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # 忽略请求不安全证书?

headers = {
    'Host': 'bing.ioliu.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '_ga=GA1.2.1389080226.1586346124; _gid=GA1.2.1179718529.1586346124; Hm_lvt_667639aad0d4654c92786a241a486361=1586346124; likes=; Hm_lpvt_667639aad0d4654c92786a241a486361=1586347115',
    'If-None-Match': 'W/"5ae9-A6K6aP64lqd/8LCoQ4XYnQ"'
}

# 1. 访问首页

url = "http://bz.0713cms.cn/"

# 获取页面
res = requests.get(url=url,header=headers,verify=False)

# 解析HTML
html_bz = html.etree.Html(res.text)   #html库中etree可以解析HTML
piclist = html_bz.xpath('//img/@scr')

print(piclist)


# 2.获取每个壁纸的url
for pic in piclist:
    pic.split()