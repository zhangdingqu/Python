#coding=gb2312
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ua='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/66.36'
options=webdriver.ChromeOptions()#实例化一个web浏览器对象[选项] 带参数启动
options.add_argument('user-agent='+ ua)#添加浏览器UA
options.add_argument("--proxy-server=http://113.121.113.215:4276")#添加浏览器代理IP
driver=webdriver.Chrome(options=options)#实例化浏览器对象 deiver
html=driver.get('http://vip.909tk.com:16880/')#请求网页
wait=WebDriverWait(driver,100)
input=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#TAB_PicTab > tbody > tr')))
print('加载出来了')


driver.close()#关闭浏览器