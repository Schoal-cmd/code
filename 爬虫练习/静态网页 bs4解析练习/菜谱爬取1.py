import requests
from bs4 import BeautifulSoup

#获取
res=requests.get('http://www.xiachufang.com/explore/')
#解析
soup=BeautifulSoup(res.text,'html.parser')
#提取1
items=soup.find_all('div',class_='info pure-u')
print(items)
#提取2
