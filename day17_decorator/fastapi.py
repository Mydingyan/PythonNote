# -*- coding:utf-8 _*-
"""
@author:Yan-PC
@file: fastapi.py
@time: 2023/5/19 23:07
"""

from fastapi import FastAPI   #轻量级高性能的web服务器框架
import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
#  这里写具体的业务
    return("hello":"auto test")


if __name__ == "__main__":
    uvicorn.run(app,host = '127.0.0.1',port = 8000)



