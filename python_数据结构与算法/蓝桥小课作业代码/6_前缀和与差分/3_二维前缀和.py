# 输入处理，读取n、m和q
n, m, q = map(int, input().split())

# 初始化数组a和二维前缀和sum
a = [[0] * (m + 1) for _ in range(n + 1)]  # 使用n+1行，m+1列的二维数组
sum_ = [[0] * (m + 1) for _ in range(n + 1)]  # 前缀和数组，同样是n+1行，m+1列

# 输入二维数组a，并计算前缀和sum_
for i in range(1, n + 1):
    a[i] = [0] + list(map(int, input().split()))
    for j in range(1, m + 1):
        sum_[i][j] = sum_[i][j - 1] + a[i][j]  # 一维前缀和处理
    for j in range(1, m + 1):
        sum_[i][j] += sum_[i - 1][j]  # 二维前缀和处理
print(a)
print(sum_)
# 查询处理
def get_sum(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:  # 越界处理
        return 0
    return sum_[x2][y2] - sum_[x1 - 1][y2] - sum_[x2][y1 - 1] + sum_[x1 - 1][y1 - 1]  # 计算矩形区域和

# 处理q次查询
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())  # 输入查询的坐标 (x1, y1) 到 (x2, y2)
    print(get_sum(x1, y1, x2, y2))  # 输出结果
