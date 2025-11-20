

n,m=map(int,input().split())
mp=[]
for i in range(n):
  mp.append([int(x) for x in input().split()])
cent=0
for i in range(n): ##向下循环搜索行
  for j in range(m): ##向右循环搜索列
    for p in range(1,min(n-i,j+1)):  ##用min（）函数设置边界条件：向下不超过n（i+p<n)(p<n-i);向左不超过0（j-p>=0)(p<=j)(p<j+1)
      if mp[i][j]==mp[i+p][j-p]: ##向下，向左移动等距离（+p；-p）
        cent+=1
    for q in range(1,min(n-i,m-j)): ##j+p<m p<m-j
      if mp[i][j]==mp[i+q][j+q]:
        cent+=1 ##向下，向右等距离移动（+p;+p)
print(cent*2)




#两个对角线上的数＋元素相等满足条件
#左对角线上的数满足j－i，并非只有主对角线
#同理，右对角线上的数满足i+j




from collections import Counter,defaultdict

n,m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
ans = 0
right = defaultdict(Counter)
left = defaultdict(Counter)#为0时不报错
for i in range(n):
    for j in range(m):
        x = g[i][j]
        ans += right[i+j][x] + left[j-i][x] ### 先累加再更新，防止对自身元素的重复计算
        #print(ans,right,left)   ### 有4个相同元素，可以组成的对数=3+2+1,，因此采用对counter循环累加再加到ans上，先累加再更新
        right[i+j][x] += 1#统计g【i】【j】在右对角上出现的次数(不包括本身）（数目循环累加得出，而不是一次算出来）
        left[j-i][x] += 1#统计x在左对角线上出现次数
print(ans*2)