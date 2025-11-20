import sys
n,m,k=map(int,sys.stdin.readline().split())
mod=int(1e9)+7
f=[0]*(n+1) ##到第x层的方法数f（x）
s=[0]*(n+1) ##到第x层的方法数f（x）的前缀和

f[1]=s[1]=1
for i in range(2,n+1):
    r=max(0,i-m)
    l=max(0,i-k-1)
    f[i]=(s[r]-s[l]+mod)%mod     ##差分
    s[i]=(s[i-1]+f[i]+mod)%mod   ##递推
print(f[n])