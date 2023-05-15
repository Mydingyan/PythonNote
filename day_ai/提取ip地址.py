# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: 提取ip地址.py
@time: 2023/3/30 15:58
"""

import re

# 示例日志
log = '20230330010010 223.104.149.43 cos.loveloveme.cn /2023/03/29/91ad731639b8c.gif 459 120 1046 206 https://www.xooznnfuvqvl.buzz:8/vodata/32180/play.html?32180-0-1 1 "Mozilla/5.0 (Linux; Android 9; V1809A Build/PKQ1.181030.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.1.20.0" "786432-786432" GET HTTPS hit 56845
20230330010010 223.104.149.43 cos.loveloveme.cn /2023/03/29/91ad731639b8c.gif 459 120 1046 206 https://www.xooznnfuvqvl.buzz:8/vodata/32180/play.html?32180-0-1 1 "Mozilla/5.0 (Linux; Android 9; V1809A Build/PKQ1.181030.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.1.20.0" "786432-786432" GET HTTPS hit 56845
20230330010011 36.161.111.172 cos.loveloveme.cn /2023/03/29/91ad731639b8c.gif 228 121 1046 304 https://www.ttqgjyjzuoqw.buzz:8/ 1 "Mozilla/5.0 (Linux; U; Android 9; zh-CN; STK-AL00 Build/HUAWEISTK-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 UCBrowser/15.3.6.1226 Mobile Safari/537.36" "(null)" GET HTTPS hit 52279
20230330010011 223.104.149.43 cos.loveloveme.cn /2023/03/29/91ad731639b8c.gif 229 120 1046 304 https://www.xooznnfuvqvl.buzz:8/vodata/32179/play.html?32179-0-1 2 "Mozilla/5.0 (Linux; Android 9; V1809A Build/PKQ1.181030.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.1.20.0" "(null)" GET HTTPS hit 56845
20230330010012 223.104.149.43 cos.loveloveme.cn /2023/03/29/91ad731639b8c.gif 0 120 1046 206 https://www.xooznnfuvqvl.buzz:8/vodata/32180/play.html?32180-0-1 1 "Mozilla/5.0 (Linux; Android 9; V1809A Build/PKQ1.181030.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.1.20.0" "786432-4999999" GET HTTPS hit 56845
'
# 匹配IP地址
ip_list = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', log)

# 打印IP地址列表
print(ip_list)