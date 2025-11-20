#区间覆盖模板问题
n,m=map(int,input().split())
a=[]
s=[]
for i in range(n):
    ai,si=map(int,input().split())
    a.append(ai)
    s.append(si)

def check(t):
    v=[]
    for i in range(n):
        if t>=s[i]:
            vi=(a[i]-(t-s[i]),a[i]+(t-s[i]))
            v.append(vi)
    v.sort()
    if len(v)==0 or v[0][0]>1:
        return False
    r=v[0][1]
    for i in range(1,len(v)):
        if v[i][0] <= r+1:
            r=max(r,v[i][1])
        else:
            break
    return r>=m

l,r=1,2000000000
while l<r:
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid+1
print(r)