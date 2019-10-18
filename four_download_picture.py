# @File  : four_download_picture.py
# @Author: Jie Wei
#@time: 2019/10/10 17:19


import pandas as pd

import os


'''使用Tor'''
from stem import Signal
from stem.control import Controller
import socket
import socks
import requests
controller = Controller.from_port(port=9151)  # 9151
controller.authenticate()
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)  # 8123  9150
socket.socket = socks.socksocket

def download_picture(file_name):
    df1 = pd.read_excel(f'./commodity/{file_name}_commodity.xlsx')
    if os.path.exists(f'./picture/{file_name}'):
        os.chdir(f'./picture/{file_name}')
    else:
        os.mkdir(f'./picture/{file_name}')
        os.chdir(f'./picture/{file_name}') #将文件的路标切换到日期文件夹下。

    for name, each_list in enumerate(list(df1.img_url)):
        print('正在下载的图片链接', each_list)

        ip = requests.get("http://checkip.amazonaws.com").text
        print(f"第{name}次使用代理IP：", ip)  # 查看包装的IP是
        controller.signal(Signal.NEWNYM)

        r = requests.get(each_list)
        with open(f'./{name}.png', 'wb') as f:
            f.write(r.content)

if __name__ == '__main__':
    import time
    fileName_date = time.strftime("%Y-%m-%d", time.localtime())  # str格式
     # 第一步先新建日期文件夹用来保存图片的
    #第二步下载图片
    download_picture(fileName_date)