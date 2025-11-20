##求阶乘
n=int(input())
ans=1
for i in range(1,n+1):
  ans*=i
print(ans)

##省赛中用杨辉三角递推求组合数：C(n,k)=C(n−1,k−1)+C(n−1,k)
###隐式定义边界
def init_C(n): # 求一个 n x n的杨辉三角
    C=[[0]*(n+1) for _ in range(n+1)]
    # 初始化 C[0][0] 为 1
    C[0][0] = 1
    # 填充杨辉三角
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C
n,m=map(int,input().split())
c=init_C(n+1)
print(c[n+1][m+1])

###显示定义边界
def init_c(n,m,mod):
  c=[[0]*(m+1) for _ in range(n+1)]
  for i in range(n+1):
    for j in range(m+1):
      if j==0:
        c[i][j]=1
      elif i==j:
        c[i][j]=1
      else:
        c[i][j]=(c[i-1][j]+c[i-1][j-1])%mod ##计算过程中取模
  return c

n,m,mod=map(int,input().split())
c=init_c(n,m,mod)
num=c[n][m]
print(num%mod)

####递归
###递归深度限制，数据大时容易超出运行时间要求
t = int(input())

def C(n ,m):
    if n == m or m == 0:
        return 1
    return C(n - 1, m) + C(n - 1, m - 1)

for _ in range(t):
    n, m = map(int, input().split())
    print(C(n, m))


###？
for i in range(t):
  n, m = list(map(int, input().split()))

  N = 1
  M = 1
  N_M = 1

  for j in range(2, n + 1):
    N = N * j

  for j in range(2, m + 1):
    M = M * j

  for j in range(2, n - m + 1):
    N_M = N_M * j

  print(int(N / (M * N_M)))

####
n,m,c=list(map(int,input().split()))
M=min(m,n-m)
fz=1
fm=1
for i in range(1,M+1):
  fm*=i
for i in range(n-M+1,n+1):
  fz*=i
print(fz//fm%c)



from math import comb
n,m,c = map(int,input().split())
print(comb(n,m)%c)