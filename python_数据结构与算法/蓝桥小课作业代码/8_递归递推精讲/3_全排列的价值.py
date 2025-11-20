## 数学计算得到递推公式: f(n+1)=f(n)*(n+1)+(n+1)![(n+1)*n]/2
## 运用递归思想
MOD = 998244353

def main():
  n = int(input())
  f = [0] * (n + 1)  # 用于存储 f[i] 的数组
  f[1] = 0
  p = 1  # 阶乘初始化为 1
  
  for i in range(1, n):
    p = p * i % MOD
    f[i + 1] = (i * (i + 1) // 2 % MOD * p % MOD + f[i] * (i + 1) % MOD) % MOD
  print(f[n])

if __name__ == "__main__":
  main()



### 正排序和反排序的价值相加为一个定值，n个数有n!个排列方式，共n!/2对排列式
### 由完全顺序排列可知，一对排列式的总价值为n（n-1）/2
### 所以总价值为n！n（n-1）/4
n=int(input())
s=n*(n-1)/4
for i in (1,n+1):
  s*=i ##n阶乘
  s=s%998244353
print(int(s))