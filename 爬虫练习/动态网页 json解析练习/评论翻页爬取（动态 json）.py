import requests

all_comment=[]
url='https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
#伪装请求头
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }

for i in range(2):
    #获取
    params={
    'g_tk':'5381',
    'loginUin':'0', 
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'GB2312',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0',
    'cid':'205360772',
    'reqtype':'2',
    'biztype':'1',
    'topid':'102065756',
    'cmd':'6',
    'needmusiccrit':'0',
    'pagenum':str(i),
    'pagesize':'15',
    'lasthotcommentid':'song_102065756_3202544866_44059185',
    'domain':'qq.com',
    'ct':'24',
    'cv':'10101010'   
    }
    res_comment=requests.get(url,headers=headers,params=params)
    #print(res_comment.url)

    #解析
    json_comment=res_comment.json()
    #print(json_comment)
    
    #提取
    list_comment=json_comment['comment']['commentlist']
    #print(list_comment)
    for comment in list_comment:
        all_comment.append(comment['rootcommentcontent'])
        all_comment.append('-----------------------------------')

#储存
print(all_comment)

    
