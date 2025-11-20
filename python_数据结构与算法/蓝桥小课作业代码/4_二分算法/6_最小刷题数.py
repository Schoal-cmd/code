##法二：100%
import bisect
def check(x,b,n):
  greater=n-bisect.bisect_right(b,b[x])
  lower=bisect.bisect_left(b,b[x])
  if lower>greater:
    return 1
  if lower<greater:
    return -1
  else:
    return 0

n=int(input())
a=[int(x) for x in input().split()]
b=sorted(a)
l,r=0,n
while l<r:
  mid=(l+r)//2
  result=check(mid,b,n)
  if result==1 or result==0:
    r=mid
  else:
    l=mid+1
m=b[r]

num=[]
result=check(r,b,n)
for i in range(n):
  if a[i]>=m:
    num.append(0)
  elif a[i]<m and result==0:
    num.append(m-a[i]+1)
  elif a[i]<m  and result==1:
    num.append(m-a[i])
print(*num)




##法一：30%通过率
def check(x,i,a):
  tot1=0
  tot2=0
  a_i=a[i]+x
  for j in a:
    if j > a_i:
      tot2+=1
    elif j<a_i:
      tot1+=1
  if tot1>=tot2:
    return True
  else:
    return False

def search(i,a,n):
  l,r=0,n-1
  while l<r:
    mid = (l + r) // 2
    if check(mid,i,a):
      r=mid
    else:
      l=mid+1
  return r


n=int(input())
a=[int(x) for x in input().split()]
num=[]
for i in range(n):
  x=search(i,a,n)
  num.append(x)
print(*num)
