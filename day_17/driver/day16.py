#!/usr/bin/python
# coding=utf-8
'''
@Author  : 乐搏-知行
@Time    : 2022/4/25 8:15
@File    : day16.py
'''
import requests

'''
爬虫项目
爬虫学得好 ...吃的早

基本原则:
1.不能影响网站的正常运作
2.不能窃取保密数据.


步骤:
1.手工实现数据采集
2.编写脚本自动获取

天天基金网
https://fund.eastmoney.com/

selenium
不用构建header,

搭建selenium环境
1.安装selenium库
pip3 install selenium

2.下载浏览器驱动程序
(1)跟浏览器种类匹配
(2)跟浏览器的(大)版本匹配   99.0.4844.51
http://npm.taobao.org/mirrors/chromedriver/
将chromedriver.exe 放在 python.exe 的目录下.
 
(3)最好关掉浏览器的 自动更新


'''

# selenium


# <a style="width:90%;line-height:20px;"
# title="华夏成长证券投资基金2021年第2季度报告"
#    href="http://fund.eastmoney.com/gonggao/000001,AN202107201504975905.html">华夏成长证券投资基金2021年第2季度报告</a>

# <a href="https://pdf.dfcfw.com/pdf/H2_AN202107201504975905_1.pdf?1626789183000.pdf">
# 查看PDF原文</a>


from selenium import webdriver
from bs4 import BeautifulSoup

# 初始化selenium
def init_selenium():
    browser = webdriver.Chrome()
    return browser

# 解析出下载信息
def get_page_report(soup_bady):

    list_result =[]
    soup_tbady=soup_bady.find_all("table",class_="w782 comm jjgg")[0].find_all("tbody")[0]
    all_tr = soup_tbady.find_all("tr")
    for one_tr in all_tr:
        #print(one_tr)
        # 获取报告的 题目
        soup_a = one_tr.find_all("td")[0].find_all("a")
        title = soup_a[0].get("title")

        # 获取报告url
        if len(soup_a)==2:
            link = soup_a[1].get("href")
        else:
            link = None

        # 获取报告日期
        data_str = one_tr.find_all("td")[2].get_text()

        # 不要摘要,只要报告
        if not title.endswith("摘要"):
            list_result.append([title,link,data_str])

    return list_result

# 获取页面代码 进行分析
def craw_report(browser,url):
    browser.get(url)
    content = browser.page_source
    soup_bady = BeautifulSoup(content,"html.parser")
    # 获取pdf的url列表
    all_report_list = get_page_report(soup_bady)
    return all_report_list

# 下载并保存报告
def get_file(report_url,save_path):
    report_num = 1
    for one_report in report_url:
        print(f"正在下载 {report_num}/{len(report_url)} 报告...")
        report_num += 1
        report_title = one_report[0]
        report_url = one_report[1]

        res = requests.get(report_url)
        with open(f"{save_path}/{report_title}.pdf",'wb') as f:
            f.write(res.content)

if __name__ == '__main__':

    code="000009"
    url = f"https://fundf10.eastmoney.com/jjgg_{code}_3.html"

    # 初始化selenium
    browser = init_selenium()

    # 用selenium获取url等参数
    all_report = craw_report(browser,url)
    print(all_report)

    # 用selenium下载数据    # 保存数据
    get_file(all_report, "../../../Desktop/22期课堂笔记/day16爬虫/report")

    # 关闭标签页
    # browser.close()
    # 退出整个浏览器
    browser.quit()

