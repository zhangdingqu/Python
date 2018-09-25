#coding=utf-8
import requests
from pyquery import PyQuery as pq
#创建反爬信息
headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}


def main():
    #请求网页
    responses=requests.get('https://item.taobao.com/item.htm?spm=a1z09.2.0.0.3cc62e8dtr6qdN&id=546395235040&_u=n1gre1je7845',headers=headers)
    #获取网页源代码
    html=str(responses.text)
    #提取主图到list
    # print(html)
    #提取sku图到list
    doc=pq(html)
    print(doc("#J_isku .J_Prop_Color li a"))

    #保存图片到文件夹


if __name__ == '__main__':
    main()

    #未完成..待续...