# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_12_01_requests(get不带参数).py
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

#请求
response = requests.get("https://www.baidu.com")

# 响应的常见用法
# print(response)    #返回请求响应码
# print(response.url)  # 返回请求地址                                                                  #str
# print(response.text)  #返回网页html源码                                                              #bytes
# print(response.content.decode("utf-8"))  # 返回html源码,并将字符编码转换成utf-8
#
# #常见字符集: UTF-8,GBK,GB2312,ASII,ISO-8859-1
#
# print(response.encoding)   # 返回服务器默认使用状态码 ISO-8859-1（导致乱码）
# print(response.headers)    #h 服务器返回的响应头
# print(response.apparent_encoding)   # 返回服务器分析出的字符编码  utf-8
#
# print(response.content.decode(response.apparent_encoding))  #根据服务器分析的编码并返回html编码（自动转换成UTF-8)      .编码为response获取的编码

# 将响应内容写入指定的HTML文件
# 将response请求的内容，写入baidu0913.html文件
# with open("baidu0913.html","w",encoding="utf-8") as f:
#     f.write(response.content.decode("utf-8"))   #write 表示写


print("======request请求案例======")
# # 用请求头把自己伪装成一个浏览器
url = r"https://www.baidu.com"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}          #表示告诉服务器，我这是“浏览器”请求的

# 有请求头(伪装成浏览器得到的结果更多)
response = requests.get(url=url,headers = header)     #位置参数可能会对不上,关键字在这里更好用
print(response.content.decode(response.apparent_encoding))    #baiduheader.html文件  (

# 没有请求头
# response = requests.get(url=url)
# print(response.content.decode(response.apparent_encoding))    #没有有请求头返回的文件baidu041802.html   和baiduheader.html文件不一样

with open("baiduheader.html","w",encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))

# # response = requests.get(url=url)

