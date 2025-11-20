#法一：与二分无关
##一
n=int(input())
a=[]
b=[]
for i in range(n):
  A,B=map(int,input().split())
  a.append(A//B)
  b.append(A//(B+1))
print(max(b)+1,min(a))
##二
import sys
n = int(sys.stdin.readline().strip())
mn, mx = 0, 10**9
for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    mn = max(mn, (a // (b + 1)) + 1)
    mx = min(mx, a // b)
print(mn, mx)


#法二：两次二分分别找出最大和最小
n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]


def check(x):
    for i in ab:
        if (i[0] // x) != i[1]:
            if (i[0] // x) > i[1]:
                return 1 ##说明v太小了，应该更更，往右找
            else:
                return -1  ##说明v太大了，应该更小，往左找
    return 0


left = 1
right = max(max(ab))
while left <= right:
    mid = (left + right) // 2
    res = check(mid)
    if res == 1:
        left = mid + 1
    else:
        if res == 0:
            mn = mid
        right = mid - 1  # 因为满足情况继续移动right 所以找的是最小值min

left = 1
right = max(max(ab))
while left <= right:
    mid = (left + right) // 2
    res = check(mid)
    if res == -1:
        right = mid - 1
    else:
        if res == 0:
            mx = mid
        left = mid + 1  # 因为满足情况继续移动left 所以找的是最大值max

print(mn, mx)


#我的代码
n=int(input())
aa=[]
bb=[]
for _ in range(n):
  a,b=map(int,input().split())
  aa.append(a)
  bb.append(b)

def check(i,n,aa,bb):
  mn=(aa[i]//(bb[i]+1)+1)
  mx=(aa[i]//bb[i])
  print(mn,mx)
  s=set()
  for x in range(mn,mx+1):
    s.add(x)
    print(s)
  return s

s=set()
s=check(0,n,aa,bb)
for i in range(n):
  s=check(i,n,aa,bb)&s
  print(s)
mn=min(s)
mx=max(s)
print(mn,mx)




#我的代码
n=int(input())
aa=[]
bb=[]
for i in range(n):
  a,b=map(int,input().split())
  aa.append(a)
  bb.append(b)

def check(x,n,aa,bb):
  for i in range(n):
    if aa[i]//x>bb[i]:
      return 1
    elif aa[i]//x<bb[i]:
      return -1
    else:
      continue
  return 0

l,r=0,max(aa)
while l<=r:
  mid=(l+r)//2
  if check(mid,n,aa,bb)==1:
    l=mid+1
  else:
    r=mid-1
    if check(mid,n,aa,bb)==0:
      mn=mid

l,r=0,max(aa)
while l<=r:
  mid=(l+r)//2
  if check(mid,n,aa,bb)==-1:
    r=mid-1
  else:
    l=mid+1
    if check(mid,n,aa,bb)==0:
      mx=mid

print(mn,mx)