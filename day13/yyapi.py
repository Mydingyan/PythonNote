# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: yyapi.py
@time: 2022/9/19 14:40
"""

import requests

# 请求URL
url = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=500&rank_role=1&skin=1"

# 请求头
payload={}
headers = {
   't': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2NzMwNTEsIm5iZiI6MTY2MzU3MDg1MSwiaWF0IjoxNjYzNTY5MDUxLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjoyNDI2NzM5MDcsImRlYnVnIjoiIiwibGFuZyI6IiJ9.GBHywH_YmmAXBBwHN3ADTxMeAZCbQMtD66d7kk_Q5j8',
   'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'
}

# 循环请求
for val in range(1,10000,1):
    print(f"第{val}次请求")
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


