#coding=utf-8
from selenium import webdriver
import requests
ua='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/66.36'
options=webdriver.ChromeOptions()#实例化一个web浏览器对象[选项] 带参数启动
options.add_argument('user-agent='+ ua)#添加浏览器UA
options.add_argument("--proxy-server=http://118.254.113.92:4283")#添加浏览器代理IP
driver=webdriver.Chrome(options=options)#实例化浏览器对象 deiver
driver.get('http://www.baidu.com')#请求网页
driver.close()#关闭浏览器
