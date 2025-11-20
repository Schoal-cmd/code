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
list_all=[]
for item in items:
    tag_a=item.find('a')
    name=tag_a.text.strip
    url='http://www.xiachufang.com'+tag_a['href']
    tag_p=item.find('p',class_='ing ellipsis')
    ingredients=tag_p.text.strip
    list_all.append([name,url,ingredients])
print(list_all)