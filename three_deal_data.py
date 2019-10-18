# @File  : three_deal_data.py
# @Author: Jie Wei
#@time: 2019/10/10 15:33

import pandas as pd

def deal_data(date_name):
    df1=pd.read_csv(f'./data/{date_name}.csv')
    list_id=df1.RECENT_EXAMPLES.apply(lambda x : eval(x))
    list_img=df1.IMG_EXAMPLES.apply(lambda x : eval(x))
    df1['list_id']=list_id
    df1['list_img']=list_img
    s = df1.apply(lambda x: pd.Series(x['list_id']),axis=1).stack().apply(lambda x: 'https://cn.tophatter.com/lots/'+str(x)).reset_index(level=1, drop=True)
    s.name = 'commidity_id'
    res=df1.drop('list_id', axis=1).join(s)
    s2 = df1.apply(lambda x: pd.Series(x['list_img']),axis=1).stack().reset_index(level=1, drop=True)
    res['img_url']=s2
    res3=res.reset_index(drop=True)
    res4=res3.drop(['RECENT_EXAMPLES','IMG_EXAMPLES','list_img'],axis=1)  #删除多列。
    res4.to_excel(f'./data/{date_name}.xlsx',index=False) #不要索引了
if __name__ == '__main__':
    import time
    date_name=time.strftime("%Y-%m-%d", time.localtime())
    print(date_name)
    deal_data(date_name)