# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day07_03_文件的初级应用.py
@time: 2022/9/3 13:21
"""

'''
# 文件的初级应用
-- ini文件的应用
-- excel 文件的应用
-- log 文件的应用
-- yaml文件的应用
'''


# 打开一个文件    示意：(文件名及路径，文件打开模式，编码方式)
# r:只读模式打开,
# 文件打开模式有：读写模式、二进制模式（比如打开图片）、文本文档模式等
# 文件句柄  ----f 表示文件代号，可以为任意内容

print("=====文件打开方式案例一：绝对路径 =======")
f = open(r"C:\Users\Administrator\PythonNote\day07\文件操作附件\微信小程序.txt",mode="r", encoding="utf-8")

# content = f.read()    #方法一：读取全部内容
# content = f.read(20)  #方法二：读取20个字符
# content = f.readline()  #方法三：读取一行内容
# print(content)
# content = f.readline()  #继续打印一行内容
# print(content)

# 使用while 循环打印多行内容
text = f.readline()
print(text)
while text != "":
    text = f.readline()
    print(text)


print("=====文件打开方式案例一：相对路径 =======")
# 相对路径（相对于 启动模块 的路径） 意思就是需要相同目录下才行
# .\ 打开同目录下文件
f = open(r".\文件操作附件\微信小程序.txt",mode="r", encoding="utf-8")

# 其他打开方式查看text_case/read+file.py文件


print("=====文件写入模式： w写案例:同名文件会被覆盖写入======")
#文件打开模式
# w 写模式   （同名的文件 会被覆盖）
# f = open(r"./文件操作附件/产品.txt",mode = 'w',encoding = 'utf-8')
#
# f.write( "111写入产品.txt的内容")  #写入内容
# f.close()  # 关闭文件（不关闭不会保存写入内容）


print("=====文件写入模式： a写案例: 能创建文件，同名的文件不会被覆盖，只会追加内容======")
#文件打开模式
# a 写模式   （同名的文件 会被覆盖）
f2 = open("r./文件操作附件/产品.txt",mode='a',encoding='utf- 8')
f2.write("这是写入的内容\n")
f2.close()

