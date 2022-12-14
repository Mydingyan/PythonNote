# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: day_13_01_邮件发送.py
@time: 2022/9/22 19:28
"""

from logging.handlers import RotatingFileHandler,SMTPHandler  # 发送邮件
import logging # python内置日志包
from logging.handlers import RotatingFileHandler, SMTPHandler   # 回滚需要这个类


# 在屏幕和日志文件同时输出log
# 用Logger配合多个handler进行复杂处理


# 1.定义一个Logger收集器
logger = logging.getLogger(__name__)

# 2.定义收集log的级别
logger.setLevel(level = logging.DEBUG)

## 2.1配置信息内容（格式化日志）
log_format = "%(asctime)s -- %(levelname)s -- %(message)s"
handler_f = logging.Formatter(log_format)

# 3. 控制台的handler
console = logging.StreamHandler()
console.setLevel(level=logging.DEBUG)

# 3.1 控制台格式化输出          # 可以选择控制台输出或者日志输出，也可以都输出
console.setFormatter(handler_f)

# 4.将handler加入到logger
logger.addHandler(console)

# 5.日志文件handler回滚
log_file = RotatingFileHandler("log4.txt",encoding="utf-8",maxBytes=1*1024*1024*1024,backupCount=2)
log_file.setLevel(logging.WARNING)

# 5.1 设置输出格式
log_file.setFormatter(handler_f)

#5.2 将handler加入到log_file
logger.addHandler(log_file)

# 6.模拟打印错误日志
logger.debug("--我是debug最低等级")
logger.info("--我是Info第二级别")
logger.warning("--我是warning第三级别")
logger.error("--我是error第四级别")
logger.critical("--我是critical最高级别")




# 发送邮件
mail_handler = SMTPHandler(
    mailhost = ('smtp.126.com',25),
    fromaddr = 'mydingyant@126.com',
    toaddrs = "mydingyant@qq.com",   #收件人
    subject = '自动化测试log',
    credentials = ("mydingyan@126.com","PUADZYMPFMNBRWGTT")   #密码T已被修改，不会发送邮件，请自定义账号密码
)

logger.setLevel(logging.ERROR)   #错误等级ERROR
logger.addHandler(mail_handler)

# 默认是warning
for i in range(5):          #每循环一次，就打印一次日志，也就循环发送一次邮件
    logger.warning("have a warning")  #warning等级不打印


logger.error("have a errpr")
logger.critical("have a critical")