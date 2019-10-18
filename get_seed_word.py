# @File  : get_seed_word.py
# @Author: Jie Wei
#@time: 2019/10/14 14:08

import pandas as pd
from four_download_picture import *
from translation.translation import *
import jieba


df1=pd.read_excel('./data/2019-10-11_total.xlsx')
S_sell_rate=df1.SELL_RATE.apply(lambda x: x.replace("%", "")).astype("float") / 100
S_price_rate=df1.ASP.apply(lambda x: x.replace("$", "")).astype("float")  #平均价格
S_AVG_SCHEDULING_FEE=df1.AVG_SCHEDULING_FEE.apply(lambda x: x.replace("$", "")).astype("float") #广告

df1['SELL_RATE']=S_sell_rate
df1['ASP']=S_price_rate
#
#
df2=df1[ (df1.SELL_RATE>0.8) & (df1.ASP>9)].sort_values("seller_lots_sold",ascending=False)  #降序排列

df3=df2.reset_index(level=0, drop=True) #将索引重置。
print(df3.title)
print(df3.title[31])
# row,col=df2.shape

from jieba import analyse
import time
def jieba_analy(x):
    translate_text = x  #1.先将文本进行翻译
    list_trans = translate(translate_text)  # 传入要翻译的文本

    time.sleep(0.5)
    keywords = jieba.analyse.extract_tags(list_trans, topK=20, withWeight=True, allowPOS=())

    return keywords

df3['seed_word']=df3.title.apply(jieba_analy)

print(df3['seed_word'])
print(df3.columns)
df4=df3[['Untitled','title','seed_word','img_url','id']] #挑出要分析的列

df4.to_excel('./commodity/1011.xlsx')
