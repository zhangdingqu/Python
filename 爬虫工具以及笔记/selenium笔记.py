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

重点//难点
1.普通定位

<input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">

driver.find_element_by_xpath('//*[@id="kw"]')
driver.find_element_by_xpath('//*[@name="wd"]')
driver.find_element_by_xpath('//*[@class="s_ipt"]')
driver.find_element_by_xpath('//*[@class="s_ipt"]')
driver.find_element_by_xpath('//input[@maxlength="100"]') # 自定义里面任何属性都可以用，但是要是唯一的！
driver.find_element_by_xpath('//input') # 只要有就找到

2.示例html层级 [xpath方式]

<div class="s_form_wrapper">
    <form id="form" class="fm" action="/s" name="f">
        <span class="bg">
            <input class="s_ipt" autocomplete="off" maxlength="255" abc="123"
                value="" name="wd">
                
driver.find_element_by_xpath('//span[@class="bg"]/input') # 定位到【class=bg】的元素里面的【input】标签
driver.find_element_by_xpath('//form[@id="form"]/span/input') # 定位到【id="form"】的元素里面的【span/input】标签

       
driver.find_element_by_css_selector()

'''