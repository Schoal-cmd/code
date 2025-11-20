def derangement(n, visited=None, current=None):
    if visited is None:
        visited = [False] * n
    if current is None:
        current = []
    
    if len(current) == n:
        print(current)
        return
    
    for i in range(n):
        if not visited[i] and (len(current) == 0 or current[0] != i):  # 确保第一个元素不与索引相同，后续元素递归处理
            visited[i] = True
            current.append(i)
            derangement(n, visited, current)
            visited[i] = False
            current.pop()

# 调用函数生成n个元素的错位排序
n = 4  # 可以修改n的值来生成不同数量的元素错位排序
derangement(n)


###因此得到递推公式： 𝐷(𝑛)=(𝑛−1)×[𝐷(𝑛−2)+𝐷(𝑛−1)]D(n)=(n−1)×[D(n−2)+D(n−1)]  边界条件： 𝐷(1)=0D(1)=0 𝐷(2)=1D(2)=1
def derangement_count(n):
    # 初始化DP数组，dp[i]表示i个元素的错位排序数量
    dp = [0] * (n + 1)
    
    # 边界条件
    dp[0] = 1  # 0个元素的错位排序数量定义为1（虽然没有实际意义，但符合递推公式）
    dp[1] = 0  # 1个元素无法进行错位排序
    
    # 使用递推公式填充DP数组
    for i in range(2, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
    
    return dp[n]

# 测试
n = 5  # 可以修改n的值来计算不同数量的元素错位排序的数量
print(f"The number of derangements for {n} elements is: {derangement_count(n)}")
print(type(derangement_count(n)))
