lst=[]
ans=0
for num in range(10,100000001):
  if len(str(num))%2==0:
    sum1=0
    sum2=0
    low=0
    high=len(str(num))
    mid=(low+high)//2
    lst=[int(i) for i in str(num)]
    for i in lst[low:mid]:
      sum1=sum1+i
    for j in lst[mid:high]:
      sum2=sum2+j
    if sum1==sum2:
      ans+=1
print(ans)

##暴力枚举，运行时间有点久，耐心等一下
