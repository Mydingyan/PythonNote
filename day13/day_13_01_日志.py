# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_13_01_日志.py
@time: 2022/9/14 22:58
"""


'''

日志：程序运行中的信息，保留在文件中

日志的等级：  机制
debug   调试     ...最多
info 信息输出
warning   警告
error   错误
critical 紧急   ...最少日志

设置warning ，就会输出其上的（warning,error,critical）等级的Log


四个组件（类）
logger  计量器，日志采集
handler 处理器，将日志发送到合适的路径
fomater 格式化器，设定日志格式
filter  过滤器

# 常用格式
format：指定输出的格式和内容，format可以输出很多有用的信息，
参数：作用 
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
'''

import logging  # python内置包




#输出一个debug信息
#1.输出日期格式
log_format = "%(asctime)s -- %(levelname)s -- %(message)s"


# 2. 将日志写入文件
log_file = "log.txt"

#3. 输出日志等级（DEBUG最低等级表示之上的日志都打印）
logging.basicConfig(filename=log_file,level=logging.DEBUG,format=log_format)



#默认不输出
# 4.需要输出的日志
logging.debug("--我是debug最低等级")       # debug和info也输出日志（一般只用在测试环境中调试）
logging.info("--我是Info第二级别")         #要注意  info是方法       logging.INFO是属性

# # 默认级别只输出以下等级日志
logging.warning("--我是warning第三级别")
logging.error("--我是error第四级别")     #可以用到异常处理
logging.critical("--我是critical最高级别")   #可以用到异常处理中


