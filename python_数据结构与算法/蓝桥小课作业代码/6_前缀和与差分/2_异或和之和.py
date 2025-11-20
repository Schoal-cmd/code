##通过率百分之六十
n=int(input())
a=[0]+[int(x) for x in input().split()]
sum=[0]*(n+1)
for i in range(1,n+1):
  sum[i]=sum[i-1]^a[i]
ans=0
for left in range(1,n+1):
  for right in range(left,n+1):
    ans+=sum[left-1]^sum[right]
print(ans)

import os
import sys

# 请在此输入您的代码

#暴力求解 40%
# n=int(input())
# a=list(map(int,input().split()))
# ans=0
# for L in range(n):
#   for R in range(n):
#     sum1=0
#     for i in range(L,R+1):
#       sum1^=a[i]
#     ans+=sum1
# print(ans)

#前缀和优化 60%
# n=int(input())
# a=list(map(int,input().split()))
# ans=0

# for L in range(n):
#   sum1=0
#   for R in range(L,n):
#     sum1^=a[R]
#     ans+=sum1
# print(ans)

#100%
n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for k in range(21):            # 所有a不超过20位
    zero, one = 1, 0           # 统计第k位的0和1的数量
    cnt, sum = 0, 0            #cnt用于统计第k位有多少对si⊕sj =1
    for i in range(n):
        v = (a[i] >> k) & 1    # 取a[i]的第k位
        sum ^= v               # 对所有a[i]的第k位做异或得到sum，sum等于0或者1
        if sum == 0:           # 前缀和为0
            zero += 1          # 0的数量加1
            cnt += one         # 这次sum=0，这个sum跟前面等于1的sum异或得1
        else:                  # 前缀异或为1
            one += 1           # 1的数量加1
            cnt += zero        # 这次sum=1，这个sum跟前面等于0的sum异或得1
    ans += cnt * (1 << k)      # 第k位的异或和相加
print(ans)

n = int(input())
N = 100010
a = [[0] * 25 for _ in range(N)]     ##开数组
b = list(map(int, input().split()))  ##获取数组Ai

for i in range(1, n + 1):
    x = b[i-1]                       ##逐一取数组内的元素
    for j in range(21, -1, -1):      ##从低位开始取元素的二进制值
        a[i][j] = (x >> j) & 1       ##取到的元素放入数组a
        a[i][j] ^= a[i - 1][j]       ##直接对第j位的01数组求前缀异或（则a数组储存了20个子数组的前缀异或）
ans = 0
for j in range(21, -1, -1):
    m = {0: 1}                       ##用哈希表存储第k位的x值
    for i in range(1, n + 1):        ##双层循环嵌套，实现一列一列查询
        x = m.get(a[i][j] ^ 1, 0)    ##先获取上一次x值，因为初始为1，所以其实消除影响了
        ans += (1 << j) * x          ##实现2**i * x
        m[a[i][j]] = m.get(a[i][j], 0) + 1  ##最后再对x进行累加
print(ans)