n=int(input())
lst=[]
for i in range(n):
  lst.extend([int(x) for x in input().split()])

lst.sort()

for i in range(1,len(lst)):
    if lst[i]-lst[i-1]!=1: ##f这里断号逻辑有误
        if lst[i]==lst[i-1]:
            num2=lst[i]
        elif:
            num1=lst[i]-1

print(num1,num2)

n=int(input())
lst=[]
for i in range(n):
    lst.extend([int(x) for x in input().split()])
lst.sort()
for i in range(min(lst),max(lst)):
    if lst.count(i)==0:
        q=1
    if lst.count(i)==2:
        p=i
print(q,p)