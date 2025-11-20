##九进制转十进制
num=2022
lst=[]
while num>=1:
  lst.append(num%10)
  num=num//10
R=9
ans=0
x=0
for i in lst:
  x=i*(R**ans)+x   #从最低位开始计算
  ans+=1
print(x)


#十进制转R进制
dict={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def _10_to_R(R:int,num:int):
    lst=[]
    if num==0:
        lst.append(0)
    while num>0:
        a=num%R
        lst.append(str(a))
        num=num//R
    print(lst)
    a=''.join(lst)
    num_R=int(a)
    return num_R

## 字符转换为二进制：
print(f"{7:b}")

##2024的二进制表达中有多少个1
num=f'{2024:b}'.count('1')
print(num)