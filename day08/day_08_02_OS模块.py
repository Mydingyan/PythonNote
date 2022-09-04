# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_08_02_OS模块.py
@time: 2022/9/4 13:46
"""

'''
文件  OS模块
OS： opreate system
Python标准库中的  用户访问操作系统的模块
'''

import  os

#查看操作系统类型
print(os.name)   #打印NT：表示Windows   ；打印posix：表示Linux 、unix 系统

#查看当前路径（运行WINDOWS CMS中的dir系统命令）
os.system("dir")

#启动程序
# os.system(r"C:\Windows\System32\calc.exe")    #打开计算器

#获取已经配置应用程序的系统变量
print(os.environ)


#获取当前Python的运行路径
print(os.getcwd())


#罗列目录下的所有文件名（非隐藏文件）
names = os.listdir(os.getcwd())
print(names)


#修改文件名
# src = r"./test_case/test_001.py"  #修改前的文件名
# dst = r"./test_case/test_101.py"  #修改后的文件名
# os.rename(src,dst)  #调用rename改名方法


# 删除文件
# os.remove(r"test_case/该删除的文件.txt")


# 给目录下的每个文件进行改名操作
dir_list = os.listdir(r"./test_case/files")
print(dir_list)

for old_name in dir_list:
    print("lod name:",old_name)
    new_name = "/rew_"+old_name   #新文件名
    os.rename("./test_case/files/"+old_name,"./test_case/files/"+new_name)  #修改前的文件路径，修改后的文件路径


# os.path() 模块
#拆分路径和文件名
file_path,file_name = os.path.split(r"C:\Users\Administrator\PythonNote\day08\test.py")
print(file_path)
print(file_name)


#判断是文件还是目录 os.listdir 方法
dir_list = os.listdir(os.getcwd())
for item in dir_list:
    if os.path.isfile(item):
        print(f"{item} is file")  #输文件名
    if os.path.isdir(item):
        print(f"{item} is dir")  #输出目录名


#判断文件是否存在  os.path.exists 方法
print(os.path.exists("day_08_01_库包模块.py"))   #存在的，返回True
print(os.path.exists("day_08_01_库包模块2.py"))  #不存在的，False
print(os.path.exists("util"))  #判断文件夹存在，返回True



# 组合文件名和路径
full_file = os.path.join(r"C:\Users\Administrator\PythonNote\day08\test_case","main_modul_001.py")
print(full_file)


# 提取文件名
file_name =  os.path.gasename
