a=5 #0101
b=3 #0011
c=-3 #11111111 11111111 11111111 11111101
print(a&b)
print(a|b)
print(a^b) #0110
print(~a) #正数的补码->得相反数
print(a<<1)
print(a>>1)
print(c>>1) #11111111 11111111 11111111 11111110
# print(c>>>1) java特有

print(0%10)
a=2025
print(a%10)
a=a//10
print(a)

for i in range(1,6):
    print(i)
