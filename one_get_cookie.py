# @File  : one_get_cookie.py
# @Author: Jie Wei
#@time: 2019/10/10 15:24


import http.cookiejar as cookielib
''' 使用Tor 洋葱头代理服务器，实现伪装IP '''
from stem import Signal
from stem.control import Controller
import socket
import socks
import requests
controller = Controller.from_port(port=9151)  # 9151
controller.authenticate()
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)  # 8123  9150
socket.socket = socks.socksocket

'''使用Tor'''
# ip = requests.get("http://checkip.amazonaws.com").text
# print("代理IP：", ip)  # 查看包装的IP是
# controller.signal(Signal.NEWNYM)

'''请求头和密码'''


def get_cookies():
    post_url="https://cn.tophatter.com/api/v1/users/authenticate.json"

    '''这个是Request Header'''
    RequestHeader={
        'Referer': 'https://cn.tophatter.com/',

        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    FormData={
            "email": 'bloomanokin@gmail.com',
            "password": 'icky-feuds-lendu-blair-9357',
        }



    '''保存cookies'''
    new_cookie_jar = requests.session()

    ip = new_cookie_jar.get("http://checkip.amazonaws.com").text
    print("代理IP：", ip)  # 查看包装的IP是
    controller.signal(Signal.NEWNYM)

    #实例化一个LWPcookiejar对象
    new_cookie_jar.cookies = cookielib.LWPCookieJar('cookie_Tor.txt')
    login_page=new_cookie_jar.post(post_url,data=FormData,headers=RequestHeader)
    print(login_page.status_code)
    #如果save()时没有写filename参数，则默认为实例化LWPCookieJar时给的文件名
    new_cookie_jar.cookies.save(ignore_discard=True, ignore_expires=True)


'''运行结束，无问题'''
if __name__ == '__main__':
    get_cookies()