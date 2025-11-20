import requests

headers={
    'referer':'https://y.qq.com/portal/search.html',
    'user-agent':'Mozilla/5.0(WindowsNT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }

for i in range(2): 
    
    #获取
    res_lyric=requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.lyric&searchid=101113619078241030&aggr=0&catZhida=1&lossless=0&sem=1&t=7&p=str(i)&n=5&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
    #解析
    json_lyric=res_lyric.json()
    #提取
    list_lyric=json_lyric['data']['lyric']['list']
    for lyric in list_lyric:
        print(lyric['content'.replace('\\n','\n')])