#coding=gb2312
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ua='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/66.36'
options=webdriver.ChromeOptions()#ʵ����һ��web���������[ѡ��] ����������
options.add_argument('user-agent='+ ua)#��������UA
options.add_argument("--proxy-server=http://113.121.113.215:4276")#������������IP
driver=webdriver.Chrome(options=options)#ʵ������������� deiver
html=driver.get('http://vip.909tk.com:16880/')#������ҳ
wait=WebDriverWait(driver,100)
input=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#TAB_PicTab > tbody > tr')))
print('���س�����')


driver.close()#�ر������