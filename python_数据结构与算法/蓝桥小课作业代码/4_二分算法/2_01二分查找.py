# 我们定义函数值域为 1,1,1,1,...,0,0,0,0
# 此时得到的ans即为最大的f(ans)=1时的ans
while l <= r:
    mid = (l + r) // 2  # 计算中间位置
    if f(mid) == 1:  # 如果 f(mid) 等于 1
        ans = mid  # 记录当前 mid
        l = mid + 1  # 向右半区间查找
    else:
        r = mid - 1  # 向左半区间查找


##对应例题：分巧克力
n, k = map(int, input().split())
chocolate = [list(map(int, input().split())) for _ in range(n)]
# print(chocolate)
front, tail = 1, 100000
def find(edge_len):
    global k
    ans = 0
    for wid, hei in chocolate:
        ans += (wid // edge_len) * (hei // edge_len)
        if(ans >= k):
            return True
    return False
while(front <= tail):
    mid = (front + tail) // 2
    if(not find(mid)):
        tail = mid - 1
    else:
        front = mid + 1
print(tail)