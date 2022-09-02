# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day07_01_草稿.py
@time: 2022/9/2 22:54
"""

# 通配符取数练习
# 总结：星号开头的，后面有1个字符，*号就代表除了最后一个的字符串
#星号在中间的，前面有几个字符占几位，后面有几个字符占中间几位，*是除了前后所有的字符串
# 星号输出的数值都是列表，无论外面是否有元组
str = "aaa","bbbb","cccc","dddd",(2022,11,11),123,55,78

*_,a = str    # 默认取最后一个值
print("*_,a这种方法取最后一个值",a)

*head,date_str = str
print("*head这种方法取出不包括最后一个值:",head)

*head,date_str,str_1,str_2 = str

print(date_str)

head,a,b,c,e,*diwuwei,mowei = str
print(diwuwei)  #打印出的元组被列表括起来

