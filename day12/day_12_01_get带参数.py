# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_12_01_get带参数.py
@time: 2022/9/13 22:02
"""

# get请求带参数的方法(URL后直接添加参数)

import requests


# get请求带参数:方法一
url = r"https://sogou.com/web?query=王者荣耀"

#get请求方法二:参数化
url = r"https://sogou.com/web"

kw = {"query":"王者荣耀"}

# 请求头
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}          #表示告诉服务器，我这是“浏览器”请求的


# 调用请求
response = requests.get(url=url,headers = header,params=kw)     # requests.get 是get请求固定写法   params=kw 方法一请求时,无需添加
print(response.content.decode(response.apparent_encoding))

# 写入文件
with open("baiduwangzherongyaoPARAMS.html","w",encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))


