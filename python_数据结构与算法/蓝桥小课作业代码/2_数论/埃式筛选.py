def sieve_of_eratosthenes(n):
    # 初始化一个布尔数组，假设所有数都是质数
    is_prime = [True] * (n + 1)
    # 0和1不是质数
    is_prime[0] = is_prime[1] = False
    
    prime = []  # 用于存储找到的质数
    
    # 从2开始检查每个数
    for i in range(2, n + 1):
        if is_prime[i]:  # 如果i是质数
            prime.append(i)  # 将i添加到质数列表中
            # 只需要检查到i*i，因为如果n是i的倍数且n < i*i，那么n已经被更小的因子标记为非质数了
            for j in range(i * i, n + 1, i): #### 精髓：步长为i
                is_prime[j] = False  # 标记i的所有倍数为非质数
    
    return prime  # 返回质数列表

# 示例用法
n = 30
print(sieve_of_eratosthenes(n))  # 输出小于或等于30的所有质数
