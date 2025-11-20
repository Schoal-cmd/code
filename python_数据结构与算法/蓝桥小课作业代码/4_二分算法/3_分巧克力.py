def chk(x, n, k, H, W):
    t = k
    for i in range(n):
        t -= (H[i] // x) * (W[i] // x)
        if t <= 0:
            return True
    return False


def main():
    # 读取 n 和 k
    n, k = map(int, input().split())

    # 读取 H 和 W 数组
    H = []
    W = []
    for _ in range(n):
        h, w = map(int, input().split())
        H.append(h)
        W.append(w)

    # 初始化二分查找的左右边界
    l, r = 1, 100000
    ans = 1

    # 二分查找
    while l <= r:
        mid = (l + r) // 2
        if chk(mid, n, k, H, W):
            ans = mid  # 更新答案
            l = mid + 1  # 向右半区间查找
        else:
            r = mid - 1  # 向左半区间查找

    print(ans)


if __name__ == "__main__":
    main()




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