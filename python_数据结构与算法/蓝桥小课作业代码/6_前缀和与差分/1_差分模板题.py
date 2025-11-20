##维护树木
# 读取输入，n是数组大小，m是查询次数
n, m = map(int, input().split())

# 初始化数组a和前缀和sum
a = [0] + list(map(int, input().split()))  # 使用n+1个位置，因为下标从1开始
sum_ = [0] * (n + 1)  # 前缀和数组，同样需要n+1个位置

# 输入数组元素，并计算前缀和
for i in range(1, n + 1):
    sum_[i] = sum_[i - 1] + a[i]  # 计算前缀和sum[i]

# 处理m次查询，输出每次区间和
for _ in range(m):
    l, r = map(int, input().split())  # 读取查询的区间 [l, r]
    print(sum_[r] - sum_[l - 1])  # 输出区间和


##求和：两两相乘再相加
n = int(input())
# 初始化数组a和sum
a = [0] + list(map(int, input().split()))  # 使用n+1个位置，因为下标从1开始
sum_ = [0] * (n + 1)  # 前缀和数组

# 初始化结果
ans = 0

# 输入数组元素并计算前缀和，同时计算结果
for i in range(1, n + 1):
    sum_[i] = sum_[i - 1] + a[i]  # 前缀和维护
    ans += a[i] * sum_[i - 1]  # 计算结果
print(ans)