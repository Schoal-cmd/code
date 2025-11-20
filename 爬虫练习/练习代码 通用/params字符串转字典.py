raw_params="""ct: 24
qqmusic_ver: 1298
remoteplace: txt.yqq.lyric
searchid: 101390884986346076
aggr: 0
catZhida: 1
lossless: 0
sem: 1
t: 7
p: 1
n: 5
w: 周杰伦
g_tk_new_20200303: 5381
g_tk: 5381
loginUin: 0
hostUin: 0
format: json
inCharset: utf8
outCharset: utf-8
notice: 0
platform: yqq.json
needNewCode: 0"""

params=dict([line.split(":",1)for line in raw_params.split("\n")])

print(params)

