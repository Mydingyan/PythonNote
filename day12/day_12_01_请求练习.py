# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_12_01_请求练习.py
@time: 2022/9/14 9:18
"""

import requests

# 老黄历请求地址
url = 'http://v.juhe.cn/laohuangli/d'

# 请求参数
kw = {"date":"2022-09-12","key":"bd24500bb902e108f3f92d1802561d94"}

# 请求头
header = {"Content-Type":"application/x-www-form-urlencoded"}

# 发送请求
# aaa = requests.get(url=url,headers=header,params=kw)
#
# # 输出结果
# print(aaa.text)

# GET新闻接口
url = "http://v.juhe.cn/toutiao/index?type=keji&page=30&page_size=30&is_filter=1&key=ee728a1f988a62f736e1f7e098fb2db1"
# url = "https://api.isoyu.com/api//Movie/playing_movie_list?start=0&count=1"
news = requests.get(url=url,headers=header)
print(news.content.decode("utf-8"))





# 成语大全
# url = 'http://apis.juhe.cn/idioms/query?wd=三心二意&key=d05c9ab6459b83eae79d576efb1fb9ec'
# url = "http://apis.juhe.cn/fapig/character_test/questions?key=de1af1d89f0388d140c21183e5124731&level=12"
# news = requests.get(url=url,headers=header)
# print(news.content.decode("utf-8"))
