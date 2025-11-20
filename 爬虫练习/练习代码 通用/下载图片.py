import requests as re

res=re.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
res1=res.content

photo=open('ppt.jpg','wb')
photo.write(res1)
photo.close()