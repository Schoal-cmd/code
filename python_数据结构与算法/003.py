n,m=map(int,input().split())
a=[]
p=[]
a.extend([int(x) for x in input().split()])
p.extend([int(x) for x in input().split()])
print(a)
### 定义排序方式
for i in range(n-1):
  for j in range(n-i-1):
    if a[j]>a[j+1] and (j+1 in p):
      a[j],a[j+1]=a[j+1],a[j]
      print(a)
    else:
        print('跳过')

### 判断+输出
b=sorted(a)
if a==b:
  exchange='YES'
else:
  exchange='NO'
print(exchange)