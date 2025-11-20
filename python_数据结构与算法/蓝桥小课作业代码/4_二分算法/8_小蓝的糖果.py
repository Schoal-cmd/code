#暴力求解 50%
n,h=map(int,input().split())
a=[int(x) for x in input().split()]

total=sum(a)
candies=[]
for i in range(n):
    tot=0
    for j in range(i,n):
        tot+=a[j]
        candy=total - tot
        if candy<=h:
            candies.append(candy)
print(max(candies))

#前缀和优化 50%
n,h=map(int,input().split())
a=[0]+[int(x) for x in input().split()]

total=0
for i in a:
    total+=i

s=[0]*(n+1)
for i in range(1,n+1):
    s[i]=s[i-1]+a[i]

candies=[]
for i in range(1,n+1):
    for j in range(i,n+1):
        tot=s[j]-s[i-1]
        candy=total-tot
        if candy<=h:
            candies.append(candy)
print(max(candies))

#分左右前缀和+结合二分 o（nlogn） 100%
n,h=map(int,input().split())
a=[0]+list(map(int,input().split()))+[0]
cnt=sum(a)-h
sums=[0]*(n+1)
for i in range(1,n+1):
    sums[i]=sums[i-1]+a[i]
sugar,ans,postion=0,0,0
for i in range(n+1,-1,-1):
    sugar+=a[i]
    if sugar>h:
        break
    l,r=0,i
    while l<=r:
        mid=(l+r)//2
        if sums[mid]+sugar<=h:
            l=mid+1
            postion=mid
        else:
            r=mid-1
    ans=max(ans,sugar+sums[postion])
print(ans)