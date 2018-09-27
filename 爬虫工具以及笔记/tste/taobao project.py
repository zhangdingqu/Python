import selenium
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ua='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/66.36'
options=webdriver.ChromeOptions()#实例化一个web浏览器对象[选项] 带参数启动
options.add_argument('user-agent='+ ua)#添加浏览器UA
options.add_argument("--proxy-server=http://182.42.45.85:9077")#添加浏览器代理IP
#http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=2&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=

driver = webdriver.Chrome(options=options)
driver.get('http://www.taobao.com')
#检测输入框有没有被加载出来
element=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.search-combobox-input-wrap > input')))
# my_input=driver.find_element(By.CSS_SELECTOR,'div.search-combobox-input-wrap > input')#获取到输入框
element.clear()#清除输入框默认值
element.send_keys(input('请输入搜索关键字:'))
driver.find_element(By.CSS_SELECTOR,'button.btn-search.tb-bg').click()#点击搜索按钮


grids1=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.grid.g-clearfix>div')))
for i in grids1.find_elements_by_css_selector('div[data-category="auctions"]'):
    my_ranks1=''#初始化淘宝店铺等级
    ranks_nobr=0#店铺等级计数
    money = i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>strong').text  # 价格
    people_Number = i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div+div').text  # 付款人数
    title = (i.find_element_by_css_selector('div.ctx-box>div.title>a').text)  # 标题
    shop_url = (i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>a').get_attribute('href'))  # 店铺首页
    chats_txt = (i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>a>span+span').text)  # 旺旺ID
    location = (i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div.location').text)  # 发货地
    for ii in i.find_elements_by_css_selector('div.ctx-box>div.g-clearfix>div>a>span.dsrs>span'):


        my_dsr_key=ii.get_attribute('class')#dsr评分
        dsr_dic={'dsr equalthan':'平','dsr morethan':'高','dsr lessthan':'低'}
        print(dsr_dic[my_dsr_key],end='')

    print(money,people_Number,title,chats_txt,location)

    # 判断是不是天猫
    my_str = ''
    t = i.find_elements(By.CSS_SELECTOR, 'ul.icons>li')
    for o in t: #店铺开通的服务
        st = o.find_element(By.CSS_SELECTOR, 'span').get_attribute('class')
        st=str(st).replace('icon-service-tianmao','天猫').replace('icon-service-jinpaimaijia','金牌卖家').replace('icon-fest-ifashion','ifashion').\
            replace('icon-service-xinpin','新品').replace('icon-service-fuwu','15天退货').replace('icon-fest-gongyibaobei','公益宝贝').replace('icon-fest-tmallzhisongonly','天猫直送')\
            .replace('icon-service-tianmaoguoji','天猫国际').replace('icon-fest-quanqiugou','全球购').replace('icon-service-remai','掌柜热卖')

        my_str = my_str + st + ','
    print(my_str[0:-1])


    if '天猫' in str(my_str):
        print('天猫')
    else:
        print('淘宝')
        chats = i.find_element_by_css_selector('div.ctx-box>div.g-clearfix>div>a>span+span') #店铺名
        ActionChains(driver).move_to_element(chats).perform()
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.ranks>span')))
        # 定位等级框内部的元素
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class^="srp-popup srp-overlay"]')))
        Random_ID = driver.find_element(By.CSS_SELECTOR, 'div[class^="srp-popup srp-overlay"]').get_attribute(
            'id')  # 查找随机ID是多少
        js = "var div = document.getElementById(\"" + Random_ID + "\");div.className = 'srp-popup srp-overlay';"  # 用JS更改class值
        driver.execute_script(js)  # 执行js脚本
        ranks = driver.find_elements_by_css_selector('a.ranks>span')
        for u in ranks:
            ranks_nobr+=1
            my_ranks=u.get_attribute('class')  # 等级集合 'icon icon-supple-level-zuan'
            my_ranks1=my_ranks1+my_ranks

        rate = driver.find_element_by_css_selector('a.ranks+span.rate').text  # 好评率：99.47%
        print(chats.text)
        print('店铺等级是:'+str(ranks_nobr)+my_ranks1.split('-')[-1].replace('xin','心').replace('zuan','钻').replace('guan','冠').replace('jinguan','金冠'))
        print(rate)
        print(driver.find_element(By.CSS_SELECTOR, 'div.m-widget-shopinfo>div+div').text.replace('\n', ',').replace('：',',').split(','))
        # ['如实描述', '4.88', '比同行均值高', '0.92%', '服务态度', '4.89', '比同行均值高', '28.66%', '物流服务', '4.87', '比同行均值高', '17.58%']

        # 获取当前随机ID值，并且展开等级框，关闭框框
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class^="srp-popup srp-overlay"]')))
        Random_ID = driver.find_element(By.CSS_SELECTOR, 'div[class^="srp-popup srp-overlay"]').get_attribute(
            'id')  # 查找随机ID是多少
        js = "var div = document.getElementById(\"" + Random_ID + "\");div.className = 'srp-popup srp-overlay srp-popup-hidden srp-overlay-hidden';"  # 用JS更改class值
        driver.execute_script(js)  # 执行js脚本
    print('========================================')

input('完事了')