# @File  : main.py
# @Author: Jie Wei
#@time: 2019/10/11 14:36

from one_get_cookie import *
from two_from_cookie_login import *
from three_deal_data import *

from five_get_json import *



import time
fileName_date=time.strftime("%Y-%m-%d", time.localtime())

print(fileName_date)

# get_cookies() #1 获取cookies  #单独运行，不然会和第四个函数起冲突。
download_data(fileName_date) #2 使用cookies登陆，爬取后台数据
deal_data(fileName_date)   #3. 对数据进行清洗，处理

# download_picture(fileName_date) #4.使用清洗的数据进行下载图片，放到筛选数据之后，再进行下载图片。

get_data_from_json(fileName_date) # 5 ，获取json数据，并将数据拼接，进行汇总。

