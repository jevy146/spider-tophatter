# @File  : five_get_json.py
# @Author: Jie Wei
#@time: 2019/10/10 17:35

import requests
'''获取json数据'''
def get_info_id(id):
    #url=f'https://cn.tophatter.com/api/v1/lots/{id}?source=&page=live_now&context=&object=&module=&slot_template=&category_filters='
    url=f'https://cn.tophatter.com/api/v1/lots/{id}'
    print(url)
    headers = {

        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}

    response = requests.get(url, headers=headers)
    text_json=response.text
    return text_json


import time,json
import pandas as pd
from pandas import Series,DataFrame


def get_data_from_json(date_file):
    df1=pd.read_excel(f'./data/{date_file}.xlsx')
    id_list=df1.commidity_id.apply(lambda x : x[-9:])  #获取商品ID
    df1['id']=id_list

    data_info=[]
    for id in id_list: #从ID的列表中
        data_1={}
        info_text=get_info_id(id)
        obj_json1=json.loads(info_text) # 将json文件转化为json格式
        data_1['id']=id
        data_1['title']=obj_json1['title']  #名称
        data_1['buy_now_price']=obj_json1['buy_now_price'] #现价
        data_1['starting_bid_amount']=obj_json1['starting_bid_amount']  #起拍价
        data_1['seller_lots_sold']=obj_json1['seller_lots_sold']  #已售数量
        data_1['alerts_count']=obj_json1['alerts_count']  #点赞人数
        data_1['shipping_price']=obj_json1['shipping_price']  #运费
        data_1['ratings_average_string']=obj_json1['ratings_average_string']  #
        data_1['calculate_ratings_count']=obj_json1['calculate_ratings_count']  #
        data_1['ratings_count']=obj_json1['ratings_count']  #
        data_1['ratings_average']=obj_json1['ratings_average']  #
        data_1['activated_at']=obj_json1['activated_at']  #
        data_1['bidding_started_at']=obj_json1['bidding_started_at']  #
        data_1['bidding_ended_at']=obj_json1['bidding_ended_at']  #
        data_info.append(data_1)
        print(data_1)
    #讲讲列表转化为DataFrame格式，以便保存
    df2=DataFrame(data_info) #

    #将两个dataframe合并。设置相同的一列
    df3=pd.merge(df1,df2,on='id')

    df3.to_excel(f'./total/{date_file}_total.xlsx',index=False)  #保存为xlsx格式
if __name__ == '__main__':
    fileName_date = time.strftime("%Y-%m-%d", time.localtime())  # str格式
    get_data_from_json(fileName_date)