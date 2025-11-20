#在n*n的点阵上取4个点作为正方形的顶点，有多少种取法
##将点换为边思考
##将正方形分类思考
##每一类只考虑独属于本身的正方形
##列举前几个找规律
n=int(input())
mod=int(1e9)+7
n-=1
sum=0
for i in range(1,n+1):
  sum+=i*(n-i+1)**2
  sum%=mod
print(sum)