def check(mid, s, n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i][j]==0:
                continue
            u = max(i - mid, 1)
            d = min(i + mid, n)
            l = max(j - mid, 1)
            r = min(j + mid, m )
            tot = s[d][r] - s[u - 1][r] - s[d][l - 1] + s[u - 1][l - 1]
            if tot >= k + 1:
                return True
    else:
        return False
    
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = [[0] * (m + 1) for _ in range(n + 1)]
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        a[i] = [0] + [int(x) for x in input().split()]
        for j in range(1, m+1):
            s[i][j] = s[i][j - 1] + a[i][j]
        for j in range(1, m+1):
            s[i][j] = s[i][j] + s[i - 1][j]

    if s[n][m] < k + 1:
        print(-1)
        continue

    l, r = 0, max(m, n)
    while l < r:
        mid = (l+ r) // 2
        if check(mid, s, n, m):
            r = mid
        else:
            l = mid + 1
    print(r)