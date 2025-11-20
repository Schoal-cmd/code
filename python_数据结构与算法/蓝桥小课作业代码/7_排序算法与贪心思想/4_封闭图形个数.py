##自定义排序
dict1={'0':1,'1':0,'2':0,'3':0,'4':1,'5':0,'6':1,'7':0,'8':2,'9':1}
n=int(input())
lst=list(input().split())
def fengbi(i):
  sum1=0
  for j in i:
    j=dict1[j]
    sum1+=j
  return sum1
res=sorted(lst,key=lambda x:(fengbi(x),int(x)))
print(*res)