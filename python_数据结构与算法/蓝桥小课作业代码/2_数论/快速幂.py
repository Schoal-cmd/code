## 利用指数的二进制表示减少乘法运算，提高效率
MOD=1
def quick_pow(a, n):
    ans = 1  # 初始化结果为1，因为任何数的0次方都是1
    while n > 0:  # 当指数n大于0时继续循环
        if n & 1:  # 如果n的当前最低二进制位为1（即n是奇数）
            ans = ans * a % MOD  # 将当前底数a乘到结果上，并取MOD的余数
        a = a * a % MOD  # 将底数a平方，并取MOD的余数，为下一轮可能的乘法做准备
        n >>= 1  # 将n右移一位（相当于n除以2），检查下一个二进制位
    return ans  # 返回最终的结果
a,n=map(int,input().split())
print(quick_pow(a,n))