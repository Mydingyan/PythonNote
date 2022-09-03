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
f2 = open(r"./文件操作附件/产品2.txt",mode='a',encoding='utf- 8')
f2.write("这是写入的内容:\n")
f2.close()



print("=====文件写入模式： r+ 读写案例: 不能能创建文件，不能追加内容，写入会重头覆盖内容======")
#r+ 读写模式
f3 = open(r"./文件操作附件/产品3.txt",mode='r+',encoding='utf-8')
f3.write("iphone 17111\n")
f3.close()


# 二进制文件如何打开
# print("=====二进制文件打开：rb、wb的使用方式=====")
#
# f4 = open(r"./文件操作附件/picture-1.jpg",mode="rb")  #读出文件路径
# f5 = open(r"./文件操作附件/picture-3-copy.jpg",mode="wb")  #复制文件路径
#
# jpg1 = f4.read()
# f5.write(jpg1)   #f5复制f4文件内容
# f4.close()
# f5.close()   #打开文件后一定要关闭，否则可能损坏文件



# 新知识：游标的使用
# seek: 光标移动字符
print("=====seek:光标移动字符位置打开文件======")
f6 = open(r"./文件操作附件/产品.txt",mode="r",encoding='utf-8')

f6.seek(6)   #光标起始位置从第几个开始（注意汉字、中英文字符占用的位置不同）   一个汉字占3位，如果输入2位，则会报错UnicodeDecodeError
content = f6.read()
print(content)
# f6.close()

print("将游标移动到：0")  #读出全部内容
f6.seek(0)
content = f6.read()
print(content)
f6.close()



# 新知识：with 打开文件省略close步骤

print("=====with语句打开文件 :可以省略close步骤，不关闭也不会报错======")
with open(r"./文件操作附件/产品.txt",mode="r",encoding='utf-8') as f7:
    f7.seek(6)
    content = f7.read()
    print(content)
    print("将游标移动到：0")
    f7.seek(0)
    content = f7.read()
    print(content)
    # f7.close()



print("=====移动光标到选择内容位置案例======")
with open(r"./文件操作附件/产品.txt",mode="r",encoding='utf-8') as f8:
    content = f8.read()  #打开文件
    loc = content.find("meta 502")   #find函数查找内容（要注意中文字符占用位置不同）
    print("-----将光标移动至meta 502前面",loc)
    f8.seek(loc)
    content = f8.read()
    print(content)






