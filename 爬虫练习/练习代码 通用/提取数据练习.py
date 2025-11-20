import requests
from bs4 import BeautifulSoup
#获取
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
#解析
soup=BeautifulSoup(res.text,'html.parser')
#提取1
items=soup.find_all(class_='books')
#提取2
for item in items:
    kind = item.find('h2') 
    title = item.find(class_='title')
    brief = item.find(class_='info') 
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)