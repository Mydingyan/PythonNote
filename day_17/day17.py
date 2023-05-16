# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day17.py
@time: 2023/5/15 21:59
"""

'''
selenium   可以理解为一个浏览器，可以控制浏览器

搭建selenium环境
1.安装selenium库  （pip3 install selenium==4.1.3 # 指定版本）
2.下载浏览器驱动程序
- 跟浏览器种类匹配
- 跟浏览器的大版本匹配
下载地址： http://npm.taobao.org/mirrors/chromedriver/
将chromedriver.exe应用程序放在python.exe 的目录下（或者放在python工程里，设置相对路径，代码执行时就不容易出现问题）


不用构建header

爬虫项目

基本原则：
1.不能影响万战的正常运作
2.不能窃取保密数据


实现爬虫的步骤：
1.手工实现数据采集
2.编写脚本自动获取

天天基金网
https://fund.eastmoney.com/
'''

# <a style="width:90%;line-height:20px;"
# title="华夏成长证券投资基金2023年第一季度报告"
# href="http://fund.eastmoney.com/gonggao/000001,AN202304211585667826.html">华夏成长证券投资基金2023年第一季度报告</a>

# <a href="https://pdf.dfcfw.com/pdf/H2_AN202304211585667826_1.pdf?1682070027000.pdf">
# 查看PDF原文</a>

# <a class="pdf" href="http://pdf.dfcfw.com/pdf/H2_AN202304211585667826_1.pdf"></a>
import requests
from selenium import webdriver
from bs4 import BeautifulSoup   #需要安装bs4  安装命令：(pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple beautifulsoup4)

# 初始化selenium
def init_selenium():
    browser = webdriver.Chrome()
    return browser


# 解析出下载信息
def get_page_report(soup_bady):

    list_result = []
    soup_tbady = soup_bady.find_all("table",class_= "w782 comm jjgg")[0].find_all("tbody")[0]
    all_tr = soup_tbady.find_all("tr")
    for one_tr in all_tr:
        print(one_tr)
        #获取报告的标题
        soup_a=one_tr.find_all("td")[0].find_all("a")
        title = soup_a[0].get("title")


        #获取报告URL
        if len(soup_a)==2:
            link = soup_a[1].get("href")    #拿到链接属性
        else:
            link = None

        # 获取报告日期
        date_str = one_tr.find_all("td")[2].get_text()

        #不要摘要，只要报告（就是过滤不想过要的数据）
        if not title.endswith("摘要"):
            list_result.append([title,link,date_str])

    return list_result

# 获取页面代码 进行分析
def craw_report(browser,url):
    browser.get(url)
    content = browser.page_source
    soup_bady = BeautifulSoup(content,"html.parser")
    #获取PDF的URL列表
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

    code = "000009"
    url = f"https://fundf10.eastmoney.com/jjgg_{code}_3.html"

    #初始化selenium
    browser = init_selenium()

    # 用selenium获取URL参数
    all_report = craw_report(browser,url)
    print(all_report)

    #用过selenium下载数据  (保存数据）
    get_file(all_report,"./report")

    #方法一：关闭标签页（没有真的关闭浏览器）
    #browser.close()
    #方法二：退出浏览器
    browser.quit()