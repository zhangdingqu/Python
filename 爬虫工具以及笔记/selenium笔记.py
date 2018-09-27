import selenium
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

ua='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/66.36'
options=webdriver.ChromeOptions()#实例化一个web浏览器对象[选项] 带参数启动
options.add_argument('user-agent='+ ua)#添加浏览器UA
driver = webdriver.Chrome(options=options)
driver.get('http://www.taobao.com')

my_input=driver.find_element(By.CSS_SELECTOR,'div.search-combobox-input-wrap > input')#获取到输入框
my_input.clear()#清除输入框默认值
my_input.send_keys('棉被')#输入框输入棉被
driver.find_element(By.CSS_SELECTOR,'button.btn-search.tb-bg').click()#点击搜索按钮

grids1=driver.find_element(By.CSS_SELECTOR,'div.grid.g-clearfix>div')
#获取单个产品的信息[第一部分]
for i in grids1.find_elements_by_css_selector('div[data-category="auctions"]'):
    #print(i.find_element_by_css_selector('div.pic-box').get_attribute('class')) #获取到pic-box部分，图片信息，没什么用
    #print(i.find_element_by_css_selector('div.ctx-box').get_attribute('class')) #获取到ctx-box部分
    money = i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>strong').text # 价格
    people_Number=i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div+div').text  # 付款人数
    title = (i.find_element_by_css_selector('div.ctx-box>div.title>a').text)  # 标题
    shop_url = (i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>a').get_attribute('href'))  # 店铺首页
    for ii in i.find_elements_by_css_selector('div.ctx-box>div.g-clearfix>div>a>span.dsrs>span'):
        print(ii.get_attribute('class'))#dsr评分

    #判断是不是天猫
    href = (i.find_element_by_css_selector('div.ctx-box>div.title>a').get_attribute('href'))  # 链接
    if 'detail.tmall.com' in href:
        print('天猫')
    else:
        print('淘宝')

    chats_txt = (i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>a>span+span').text)  # 旺旺ID
    chats=i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>a>span+span')
    location = (i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div.location').text)  # 发货地
    for iii in i.find_elements_by_css_selector('div.ctx-box>div.g-clearfix>div>ul>li'):
        print(iii.find_element_by_css_selector('span').get_attribute('class')) #开通的服务
    #还有触摸后ajax数据没有获取
    ActionChains(driver).move_to_element(chats).perform()

    #获取当前随机ID值，并且展开等级框
    Random_ID = driver.find_element(By.CSS_SELECTOR, 'div[class^="srp-popup srp-overlay"]').get_attribute('id')  # 查找随机ID是多少
    js = "var div = document.getElementById(\"" + Random_ID + "\");div.className = 'srp-popup srp-overlay';"  # 用JS更改class值
    driver.execute_script(js)  # 执行js脚本

    #合并实现展开店铺等级框
    chats = i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>a>span+span')
    ActionChains(driver).move_to_element(chats).perform()
    Random_ID = driver.find_element(By.CSS_SELECTOR, 'div[class^="srp-popup srp-overlay"]').get_attribute(
        'id')  # 查找随机ID是多少
    js = "var div = document.getElementById(\"" + Random_ID + "\");div.className = 'srp-popup srp-overlay';"  # 用JS更改class值
    driver.execute_script(js)  # 执行js脚本

        #定位等级框内部的元素
        ranks=driver.find_elements_by_css_selector('a.ranks>span')[0].get_attribute('class') #等级集合 'icon icon-supple-level-zuan'
        rate=driver.find_elements_by_css_selector('a.ranks+span')[0].text #好评率：99.47%

        print(driver.find_element(By.CSS_SELECTOR,'div.m-widget-shopinfo>div+div').text.replace('\n',',').replace('：',',').split(','))
        #['如实描述', '4.88', '比同行均值高', '0.92%', '服务态度', '4.89', '比同行均值高', '28.66%', '物流服务', '4.87', '比同行均值高', '17.58%']


#获取单个产品的信息[第二部分]
grids2=driver.find_elements(By.CSS_SELECTOR,'div.items#J_itemlistPersonality div>div.item.J_MouserOnverReq')

#获取页数
total=driver.find_element(By.CSS_SELECTOR,'div.total')
my_total=int(re.findall('\d+',total.text)[0])

#获取点击下一页按钮
driver.find_element(By.PARTIAL_LINK_TEXT,'下一页').click()#找到包含下一页文字的链接点击
 #获取当前激活的页码
item_active=int(driver.find_element(By.CSS_SELECTOR,'div.inner.clearfix >ul> li.item.active > span').text)


















'''
源码：
    <input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">

#选择器的种类
    driver.find_element_by_id("kw")
    driver.find_element_by_name("wd")
    driver.find_element_by_class_name("s_ipt")
    driver.find_element_by_tag_name("input")
源码：
    <a href="http://news.baidu.com" target="_blank" class="mnav">新闻很长的文本很长的文本</a>
语法：
    driver.find_element_by_link_text("新闻很长的文本很长的文本") # 获取新闻的链接[完全匹配]
    driver.find_element_by_partial_link_text("新闻很长的") # 部分文字匹配到获取到链接[部分匹配]

重点//难点
1.普通定位
代码：
    <input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">
语法：
    driver.find_element_by_xpath('//*[@id="kw"]')
    driver.find_element_by_xpath('//*[@name="wd"]')
    driver.find_element_by_xpath('//*[@class="s_ipt"]')
    driver.find_element_by_xpath('//*[@class="s_ipt"]')
    driver.find_element_by_xpath('//input[@maxlength="100"]') # 自定义里面任何属性都可以用，但是要是唯一的！
    driver.find_element_by_xpath('//input') # 只要有这个标签就找到

2.示例html层级 [xpath方式]
源码:
    <div class="s_form_wrapper">
        <form id="form" class="fm" action="/s" name="f">
            <span class="bg">
                <input class="s_ipt" autocomplete="off" maxlength="255" abc="123"
                    value="" name="wd">
语法：             
    driver.find_element_by_xpath('//span[@class="bg"]/input') # 定位到【class=bg】的元素里面的【input】标签
    driver.find_element_by_xpath('//form[@id="form"]/span/input') # 定位到【id="form"】的元素里面的【span/input】标签
    driver.find_element_by_xpath('//input[@abc="123"]') # 任意标签定位======================
    driver.find_element_by_xpath('//div[@class="service J_Service"]') #双class的定位方法。注意要复制哦，手动输入容易出错
3.xpath  and 方式双条件查找
源码：
    <input id="kw" name="wd">#查找这一行
    <input id="kw" name="aa">
    <input id="bb" name="wd">
语法：
    driver.find_element_by_xpath('//input[@id="kw" and @name="wd" and......]') # 重点！！！！
    driver.find_element_by_xpath('//div[@class="service J_Service" and @data-spm-ab="main"]')




4.css选择器语法css定位 ==========================
代码：
    <input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">
        <input class="s_ipt" autocomplete="off" maxlength="255" abc="123"
语法：
    driver.find_element_by_css_selector("#kw") #ID的写法
    driver.find_element_by_css_selector("[name=wd]") #name的写法
    driver.find_element_by_css_selector(".s_ipt") #class的写法
    driver.find_element_by_css_selector("[abc=123]") #自定义元素定位====
代码：
    <div class="s_form_wrapper">
        <form id="form" class="fm" action="/s" name="f">
            <span class="bg">
                <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" abc="123" value="" name="wd">
                  
语法：
    driver.find_element_by_css_selector("span.bg > input#kw ") #span标签class名叫bg > input#kw，input#kw的ID为kw
    driver.find_element_by_css_selector("[abc="123"]")========

源码：
    标签1源码：<div class="s_form_wrapper abc efj" name="wd">
    标签2源码：<ul class="service-bd" role="menubar">
语法：
    标签1定位：driver.find_element_by_css_selector("div.s_form_wrapper.abc.efj[name="wd"]")
    标签2定位：driver.find_element_by_css_selector('ul.service-bd[role="menubar"]')======
    driver.find_element_by_css_selector('div.tbh-nav.J_Module.tb-pass.tb-bg[data-name="nav"]') #标签属性多条件定位
    
    grids2.get_attribute('class') # 查看特征名称，通常是系统未定义的
    grids2.get_property('class') # 查看属性名称，通常是系统定义过的
    
兄弟选择器：
    print(driver.find_element_by_css_selector('div.grid.g-clearfix>div>div>div:nth-child(2)').get_attribute('class')) # div:nth-child(3)元素下面的第三个儿子
    print(driver.find_element_by_css_selector('div.grid.g-clearfix>div>div>div+div').get_attribute('class')) # div+div元素下面的第二个儿子


多属性开头结尾特征选择器：
源码：
    <div id="ks-component902" class="srp-popup srp-overlay srp-popup-hidden srp-overlay-hidden" style="left: 403px; top: 4134px; display: block;">
    
语法：

print(driver.find_element(By.CSS_SELECTOR,'div[class^="srp-popup srp-overlay"]').get_attribute('class')) #查找class开头为srp-popup的元素
print(driver.find_element(By.CSS_SELECTOR,'div[class$="srp-overlay-hidden"]').get_attribute('class')) #查找class末尾为srp-overlay-hidden的元素
print(driver.find_element(By.CSS_SELECTOR,'div[class*="srp-popup-hidden"]').get_attribute('class')) #查找包含srp-popup-hidden的class元素


用js改变代码属性：
源码：
    <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off" style="border: 2px solid red;">
语法：
    js="var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"   #前部分是定位目标，后部分是修改目标的属性
    driver.execute_script(js) # 执行上面的修改

taob成功语法：[注意先打印js脚本没问题后再试]

    js="var div = document.getElementById('ks-component945');div.className = 'abc';"
    driver.execute_script(js)
    
    js = "var div = document.getElementById(\"" + Random_ID + "\");div.className = 'hahaha';"#用JS更改class值
    driver.execute_script(js) #执行js脚本

'''


input("")