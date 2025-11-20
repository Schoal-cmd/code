#我的代码
n, m = map(int, input().split())
card_number = [int(x) for x in input().split()]
max_writecard_number = [int(x) for x in input().split()]


def check_suit_number(x, n, m, card_number, max_writecard_number):
    for i in range(n):
        if card_number[i] >= x:
            continue
        else:
            if (x - card_number[i]) > max_writecard_number[i]:
                return False
            else:
                m -= (x - card_number[i])
    return m >= 0


l, r = 0, 200000
ans = 0
while l <= r:
    mid = (l + r) // 2
    if check_suit_number(mid, n, m, card_number, max_writecard_number):
        ans= mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)






#参考代码
def chk(x, n, m, a, b):
    res = m
    for i in range(n):
        if x - a[i] > b[i]:
            return False
        else:
            res -= (x - a[i])
    return res > 0

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l, r = 0, 2000000
    ans = 0

    # 二分查找
    while l <= r:
        mid = (l + r) // 2
        if chk(mid, n, m, a, b):
            ans = mid  # 更新答案
            l = mid + 1  # 向右半区间查找
        else:
            r = mid - 1  # 向左半区间查找

    print(ans)

if __name__ == "__main__":
    main()