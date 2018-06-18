## Python爬虫笔记
初始化
```Python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
```
## 1、request(网络资源获取模块)
[request安装方法](https://blog.csdn.net/niepangu/article/details/78698819)  

Get获取网页示例  
```python
import requests
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'#遇到的网页时utf-8 格式
print (res.text)#获取网页源码
#print (res.encoding)查看获取网页使用的编码格式
```  
## 2、将网页读进Beautifulsoup中进行解析  
```Python
from bs4 import  BeautifulSoup #导入bs4模块
	html_sample = '<html>获取的源代码</html>'#将要解析的HTML文件赋值给html_sample
	soup = BeautifulSoup(html_sample,html.parser) # 用BeautifulSoup解析元素     [tml.parser]是指定解析器解析的是html文件
print(soup.text)#打印解析的内容
```  
- 找出所有含有特定标签的html元素  
	- 使用select 找出含有h1标签的元素  
	![Alt text](图/header.jpg)

	