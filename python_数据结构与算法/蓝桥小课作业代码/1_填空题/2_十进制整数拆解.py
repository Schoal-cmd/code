#列表推导法
num=1689
x=[int(i) for i in str(num)]
print(x)

#取模
num=1698
lst=[]
while num>0:
    lst.append(num%10)
    num=num//10
lst.reverse()
print(lst)