n,m=map(int,input().split())
a=[[0]*(n+2) for _ in range(n+2)]
s=[[0]*(n+2) for _ in range(n+2)]
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    a[x1][y1]+=1
    a[x1][y2+1]-=1
    a[x2+1][y1]-=1
    a[x2+1][y2+1]+=1

for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j]=s[i][j-1]+a[i][j]
    for j in range(1,n+1):
        s[i][j]+=s[i-1][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if s[i][j]%2==0:
            print('0',end=' ')
        else:
            print('1',end=' ')
    print()
