# @File  : get_commidity.py
# @Author: Jie Wei
#@time: 2019/10/18 10:05

import pandas as pd
from four_download_picture import *

import time
fileName_date=time.strftime("%Y-%m-%d", time.localtime())

print(fileName_date)

'''通过分析筛选出可以做的产品，然后下载图片'''
df1=pd.read_excel(f'./total/{fileName_date}_total.xlsx')
print(df1.head())
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


print(df3.columns)
df4=df3[['title','img_url','id']] #挑出要分析的列
print(df4.head())
df4.to_excel(f'./commodity/{fileName_date}_commodity.xlsx') #保存有索引

'''保存好xlsx文件后再下载图片'''
download_picture(fileName_date)  #最后下载图片