
##rn=max1<=i<=n(pi+rn-i) 优于 rn=max(pn,r1+rn-1,r2+rn-2,...,rn-1+r1)
##后者需要重复计算子问题


###自顶向下递归实现 o（2**n)
p=[0,1,5,8,9,10,17,17,20,21,23,24,30]
def cut_rod_recurision_1(p,n):
    if n==0:
        return 0
    else:
        res=p[n]
        for i in range(1,n):
            res=max(res,cut_rod_recurision_1(p,i)+cut_rod_recurision_1(p,n-i))
    return res

def cut_rod_recurision_2(p,n):
    if n==0:
        return 0
    else:
        res=0
        for i in range(1,n+1):
            res=max(res,p[i]+cut_rod_recurision_2(n-i))
        return res





###自低向下 动态规划求解

#n=int(input())
#p=[0,1,5,8,9,10,17,17,20,24,30]
#r=[0]*n
#res=0
#for i in range(1,n):    
#    res=max(res,p[i]+r[n-i])     ##一直使用一个组合情况，但n变化，组合情况变化
#    r[i]=res
#    print(r)

def cut_rod_dp(p,n):
    r=[0]
    for i in range(1,n+1):
        res=0
        for j in range(1,i+1):
            res=max(res,p[j]+r[i-j])
        r.append(res)
        print(r)
    return r[n]
cut_rod_dp(p,9)


def cut_rod_extend(p,n):
    r=[0]
    s=[0]
    for i in range(1,n+1):
        res=0
        res_s=0
        for j in range(1,i+1):
            if res<p[j]+r[i-j]:
                res=p[j]+r[i-j]
                res_s=j
            else:
                continue
        r.append(res)
        s.append(res_s)
        print(r)
        print(s)
    return r[n],s
cut_rod_extend(p,9)


def cut_rod_solution(p,n):
    result=[]
    r,s=cut_rod_extend(p,n)
    while n>0:
        result.append(s[n])
        n-=s[n]
    return result
print(cut_rod_solution(p,9))

