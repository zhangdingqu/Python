import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
'''
<input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">

#选择器的种类
driver.find_element_by_id("kw")
driver.find_element_by_name("wd")
driver.find_element_by_class_name("s_ipt")
driver.find_element_by_tag_name("input")

<a href="http://news.baidu.com" target="_blank" class="mnav">新闻很长的文本很长的文本</a>
driver.find_element_by_link_text("新闻很长的文本很长的文本")#获取新闻的链接[完全匹配]
driver.find_element_by_partial_link_text("新闻很长的")#部分文字匹配到获取到链接[部分匹配]


driver.find_element_by_xpath('//*[@id="kw"]')
driver.find_element_by_xpath('//*[@name="wd"]')
driver.find_element_by_xpath('//*[@class="s_ipt"]')
driver.find_element_by_xpath('//*[@class="s_ipt"]')

driver.find_element_by_css_selector()

'''