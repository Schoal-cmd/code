## 日期问题 月日循环

month=[31,28,31,30,31,30,31,31,30,31,30,31]
week=6
ans=0
for i in month:
  for j in range(1,i+1):
    if j==1 or j==11 or j==21 or j==31 or week==6 or week==0:
      ans+=1
    week=(week+1)%7
print(ans)