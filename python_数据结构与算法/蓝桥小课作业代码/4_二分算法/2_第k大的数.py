n,m,k=map(int,input().split())
mp=[i*j for i in range(1,n+1) for j in range(1,m+1)]
big=[]
for i in range(m*n):
  a=max(mp)
  if a not in big:
    big.append(a)
  if len(big)==k:
    print(a)
    break




def check(n, m, k, v):
    res = 0
    for i in range(1, n + 1):
        res += min(m, v // i)  ##计算乘法表中每一行比v小的数，然后累加得到整个表中比k小的数
    return res >= k ##这里取等了

def find_kth_largest(n, m, k):
    l = 1
    r = n * m
    while l < r:
        mid = (l + r) // 2
        if check(n, m, k, mid):
            r = mid ##所以再这里取等
        else:
            l = mid + 1
    return r

n, m, k = map(int, input().split())
result = find_kth_largest(n, m, k)
print(result)