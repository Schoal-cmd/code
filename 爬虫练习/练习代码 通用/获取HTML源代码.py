import requests as re 
 
res=re.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
print(res.status_code)

if res.status_code==200:
    file=open('code.html','w',encoding=res.apparent_encoding)
    file.write(res.text)
    file.close
    print('html源代码获取成功')