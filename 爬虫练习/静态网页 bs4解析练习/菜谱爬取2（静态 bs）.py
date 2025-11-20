import requests
from bs4 import BeautifulSoup

#获取
res=requests.get('http://www.xiachufang.com/explore/')
#解析
soup=BeautifulSoup(res.text,'html.parser')
#提取name url
list_all=[]
list_name=[]
list_url=[]
list_ingredients=[]
items1=soup.find_all('p',class_='name')
items2=soup.find_all('p',class_='ing ellipsis')
for item1 in items1:
    list_name.append(item1.text.strip)
    list_url.append(items1['href'])
for item2 in items2:
    list_ingredients.append(item2.text.strip)
list_all.append(list_name)
list_all.append(list_ingredients)
list_all.append(list_url)
print(list_all)
