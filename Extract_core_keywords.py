# @File  : Extract_core_keywords.py
# @Author: Jie Wei
#@time: 2019/10/18 10:56
import pandas as pd
import jieba
from jieba import analyse
'''用机器提取核心关键词'''

import time
def jieba_analy(x):

    time.sleep(0.5)
    keywords = jieba.analyse.extract_tags(x, topK=20, withWeight=True, allowPOS=())

    return keywords


fileName_date = time.strftime("%Y-%m-%d", time.localtime())  # str格式

df1=pd.read_excel(f'./commodity/{fileName_date}_commodity.xlsx')  ##2019-10-18_commodity.xlsx
df1['seed_word']=df1.title.apply(jieba_analy)
print(df1['seed_word'])

'''保存，并覆盖'''
df1.to_excel(f'./commodity/{fileName_date}_commodity.xlsx',index=False)