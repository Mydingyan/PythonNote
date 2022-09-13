# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_12_01_requests.py
@time: 2022/9/12 22:55
"""


'''
requests库

不是浏览器可以通过HTTP协议 发送网络请求,并获取返回的数据
postman\jmeter\智能手表等软硬件都可以发送网络请求


python 的requests 库 ,也可以通过HTTP协议 发送网络请求,并获取返回的数据

比urllib库,更加简单,使用方便 ,文档更全

中文官方文档: https://cn.python-requests.org/zh_CN/latest/   

安装命令: pip3 install requests

requests库  请求的构成
0:URL
1. 请求方法(GET POST   HEAD  PUT PATCH DELETE)  HEAD 头     PUT      PATCH 修改        DELETE 删除
2. 请求头(header):
User_Agent,Refer,Cookie,Accept-Encoding,Accept-Language:语言,
Content-Type:四种请求方式
- application/x-www-form-urlencoded :表单
- multipart/form-data:
- application/json:  json格式
- application/xml:xml格式

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36

3.请求体(body)
'''

import requests


response = requests.get("https://www.baidu.com")
# print(response)    #返回请求响应码
# print(response.url)  # 返回请求地址
# print(response.text)  #返回网页
# print(response.content.decode("utf-8"))  # 返回网页,并将字符编码转换成utf-8

#常见字符集: UTF-8,GBK,GB2312,ASII,ISO-8859-1

print(response.encoding)   # 获取返回的字符串编码 ISO-8859-1
print(response.headers)    #h 获取返回的头部
print(response.apparent_encoding)   # 返回字符编码

print(response.content.decode(response.apparent_encoding))  #内容.编码为response获取的编码

# 按utf-8打开本地html文件
with open("baidu.html","w",encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))

# 用请求头把自己伪装成一个浏览器
url = r"https://www.baidu.com"
header = {"User-Agent:"
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
          }

response = requests.get(url=url,header=header)

# response = requests.get(url=url)
print(response.content.decode((response.apparent_encoding)))

