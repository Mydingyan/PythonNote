# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_12_01_post请求.py
@time: 2022/9/13 22:17
"""

import requests


# post请求(方式一:字典格式传参)
# data = {"name":"lebo","age":"5"}  # post请求参数
#
# # post请求
# response = requests.post("http://httpbin.org/post",data = data)                 # http://httpbin.org/ 是练习网站
#
# print(response.text)   #输出详情


# post请求(方式二:转换成JSON格式传参)
# json格式发送post请求
import json   #需要导入json
data = {"name":"lebo","age":"5"}
url_json = "http://httpbin.org/post"
data_json = json.dumps(data)     #  把字典转换成JSON格式
# print(type(data_json),data_json)   #返回json格式

res_json = requests.post(url=url_json,data=data_json)  # 发送请求
print(res_json.text)