# @File  : __init__.py.py
# @Author: Jie Wei
#@time: 2019/10/10 15:24
import time
print(time.time())

from datetime import datetime
t=time.strftime("%Y-%m-%d", time.localtime())
print(type(t) )