# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day20.py
@time: 2023/5/25 23:00
"""

'''
selenium :用于web应用程序的测试工具，模拟手工操作浏览器，进行自动化测试

优点：
开源免费
多浏览器支持
多平台支持
支持分布式测试（Grid）
支持录制回放和脚本生成（IDE）

selenium三剑客
WebDriver
IDE ：支持录制回放和脚本生成
Grid: 支持分布式测试


官方文档：
- https://selenium-python.readthedocs.io/index.html
- https://seleniumhq.github.io/selenium/docs/api/py/api.html


webdriver工作原理：
通过浏览器的driver与浏览器进行通信（传令兵）

配置selenium环境：
pip install selenium

下载webdriver(与浏览器的 种类和版本匹配)
Chrome：http://chromedriver.storage.googleapis.com/index.html
Firefox：https://github.com/mozilla/geckodriver/releases/

安装方法一：通过上述链接下载，放置在python的安装目录中
安装方法二：放置在项目中的 专门目录中（如果写自动化项目放置在专门目录，可以防止出现问题）

'''
from time import  sleep
from selenium import webdriver

# 浏览器的无界面操作
opt = webdriver.ChromeOptions()
opt.headless = True

#1 初始化一个driver （需要添加括号）
# 需要界面(能够打开浏览器界面）
# driver = webdriver.Chrome()
# 无界面操作（不打开浏览器页面）
driver = webdriver.Chrome(options=opt)

#2.访问乐博商城
driver.get("http://shop.pro.17lebo.com")

# 设置浏览器的窗口大小  (无界面模式下，也能够调整浏览器大小）
# driver.maximize_window()
# sleep(3)
# driver.minimize_window() #窗口最小化
# driver.set_window_size(480,900)

#前进后退
# 乐博官网
driver.get("http://www.17lebo.com") #原页面上继续访问新页面
sleep(2)
driver.back()  #返回上一页面
sleep(2)
driver.forward()  #进入下一页面

# 浏览器截图（png格式）
driver.get_screenshot_as_file("浏览器截图.png")
sleep(2)
driver.get_screenshot_as_file("screenshots/浏览器截图2.png")


#刷新页面
driver.refresh()

#获取页面属性
print("网页标题：",driver.title)  #print只是为了演示driver.title获取到的内容
print("当前网址：",driver.current_url)
print("浏览器名称：",driver.name)
print("页面源码", driver.page_source.encode('utf-8'))

#关闭浏览器
sleep(5)  #等待5秒
driver.quit()  #关闭整个浏览器
# driver.close()  #关闭标签页
