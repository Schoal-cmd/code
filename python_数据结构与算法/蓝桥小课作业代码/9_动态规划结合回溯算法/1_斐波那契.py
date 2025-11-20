#用递归来写，比较耗时:子问题的重复计算
def fibnacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)

#动态规划：最优子结构/最优子问题 ；递推式+重复子问题
#贪心思想是动态规划的特例，用贪心能做到用动态规划一定能做，dp能做的贪心不一定能做
##最优子结构：原问题最优解涉及多少个子问题，在确定最优解使用哪些子问题时需要考虑多少种选择
def fibonacci_no_recurision(n):
    f=[0]*n
    f[0]=1
    f[1]=1
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
    return f
print(fibonacci_no_recurision(6))

