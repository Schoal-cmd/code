### 任意次
### 只能用数组p中的数值作为数组a中的角标进行冒泡排序

n,m=map(int,input().split())
a=[]
p=[]
a.extend([int(x) for x in input().split()])
p.extend([int(x) for x in input().split()])
print(a,p)
### 定义排序方式
while True:
  for j in range(len(a)-2):
    exchange=False
    if a[j]>a[j+1] and (j+1 in p):
      a[j],a[j+1]=a[j+1],a[j]
      exchange=True
      print(a)
  if not exchange:
    break
### 判断+输出
b=sorted(a)
if a==b:
  exchange='YES'
else:
  exchange='NO'
print(exchange)