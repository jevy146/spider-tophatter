# @File  : two_from_cookie_login.py
# @Author: Jie Wei
#@time: 2019/10/10 15:26


import requests
import http.cookiejar as cookielib
from scrapy.selector import Selector

'''使用cookie'''

def download_data(fileName_date):
    session = requests.session()
    load_cookiejar = cookielib.LWPCookieJar()
    # 从文件中加载cookies(LWP格式)
    load_cookiejar.load('cookie_Tor.txt', ignore_discard=True, ignore_expires=True)
    # 工具方法转换成字典
    load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)
    # 工具方法将字典转换成RequestsCookieJar，赋值给session的cookies.
    session.cookies = requests.utils.cookiejar_from_dict(load_cookies)

    header={
        'Referer': 'https://cn.tophatter.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }

    infoUrl = 'https://cn.tophatter.com/seller/insights/categories'
    responseJCI = session.get(infoUrl, headers=header, allow_redirects=False)
    if responseJCI.status_code != 200:
        url = responseJCI.headers['Location']  # 没登录上，需要再次登陆 cookies失效了,查看网址跳转去了哪里
        print(url)

    else:
        pass
            # print(responseJCI.text)
        '''使用xpath，直接将response传入'''
    selector = Selector(responseJCI)

    tr_list=selector.xpath('//*[@id="main"]//table/tbody/tr') #构造成为一个列表

    print('tr_list', tr_list)

    import csv
    data_info=list()
    for td_one in tr_list:
        data_item = dict()
        data_item['CATEGORY']=td_one.xpath('./td/text()').extract()[0]
        data_item['SUBCATEGORY']=td_one.xpath('./td/text()').extract()[1]
        data_item['SELL_RATE']=td_one.xpath('./td/text()').extract()[-3].strip()
        data_item['ASP']=td_one.xpath('./td/text()').extract()[-2].strip()
        data_item['AVG_SCHEDULING_FEE']=td_one.xpath('./td/text()').extract()[-1].strip()
        data_item['RECENT_EXAMPLES']=td_one.xpath('./td/a/@data-lot-id').extract() #三件产品的ID
        data_item['IMG_EXAMPLES']=td_one.xpath('./td/a/img/@src').extract() #三件产品的图片
        print(data_item)
        data_info.append(data_item) #将字典保存到列表中


        '''for循环结束后，将数据保存到本地'''
    with open(f"./data/{fileName_date}.csv", "a", encoding='utf-8', newline="")as file:
        csv.writer(file).writerow(data_info[0].keys())  #这个是表头。
        for data in data_info:
            csv.writer(file).writerow(data.values())
if __name__ == '__main__':
    import time
    fileName_date=time.strftime("%Y-%m-%d", time.localtime())  #str格式
    print(fileName_date)
    download_data(fileName_date)  #以日期格式命名