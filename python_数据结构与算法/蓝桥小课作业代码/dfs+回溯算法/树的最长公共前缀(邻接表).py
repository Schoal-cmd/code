##邻接表+dfs
##单向边
import sys
sys.setrecursionlimit(100000)

N=200010
g1=[[] for _ in range(N)]
g2=[[] for _ in range(N)]
p1=[0]*N
p2=[0]*N
res=0

n,m=map(int,input().split())
p1[1:n+1]=list(map(int,input().split()))
p2[1:m+1]=list(map(int,input().split()))

for i in range(n-1):
    u,v=map(int,input().split())
    g1[u].append(v)

for i in range(m-1):
    u,v=map(int,input().split())
    g2[u].append(v)

def dfs(st1,st2,count):
    global res
    if p1[st1]!=p2[st2]:
        return
    res=max(res,count+1)
    for i in g1[st1]:
        for j in g2[st2]:
            if p1[i]==p2[j]:
                dfs(i,j,count+1)

dfs(1,1,0)
print(res)
### 在你提供的代码中，深度优先搜索（DFS）算法确实没有显式地使用回溯算法。
### 然而，这并不意味着代码中的DFS没有回溯的逻辑。实际上，回溯通常是通过递归函数的自然结束（即递归栈的弹出）来实现的，而不是通过显式的状态重置。
#### 然而，你的代码中存在一个潜在的问题：它可能会重复访问相同的节点对(st1, st2)多次，尤其是当图g1和g2中存在环时。
#### 这是因为代码没有记录哪些节点对已经被访问过，导致DFS可能会陷入无限递归


##双向边
import sys
sys.setrecursionlimit(300000)


n,m=map(int,input().split())
a=[[] for _ in range(n+1)] ##a和b是两个图的邻接表表示。
va=[0]*(n+1)  ##va和vb是两个访问标记数组，用于跟踪哪些节点已经被访问过。
va[1]=1
c=[0]+list(map(int,input().split())) ##c和d是两个数组，存储了两个图中每个节点的值（或称为“权重”或“标签”）。

b=[[] for _ in range(m+1)]
vb=[0]*(m+1)
vb[1]=1
d=[0]+list(map(int,input().split()))
#print(a,b)

for _ in range(n-1):
    u,v=map(int,input().split())
    a[u].append(v)
    a[v].append(u)  ##注意，这里构建的是无向图，因为对于每条边(u, v)，都添加了u到v和v到u的连接。
for _ in range(m-1):
    p,q=map(int,input().split())
    b[p].append(q)
    b[q].append(p)

ans=1
def dfs(u,p,cnt): ##其中u和p分别是两个图中当前搜索的节点，cnt是当前搜索路径的长度。
    global ans
    for i in a[u]: ##首先遍历图a中当前节点u的所有邻居节点i。
        if va[i]==0:
            va[i]=1
            for j in b[p]:
                if vb[j]==0 and c[i]==d[j]:
                    #print(i,j,cnt)
                    vb[j]=1
                    ans=max(ans,cnt+1)
                    dfs(i,j,cnt+1)
                    va[i]=0  ##回溯
                    vb[j]=0

dfs(1,1,1)
print(ans)



#
import sys
sys.setrecursionlimit(90000)

N = 200010
a = [0] * N #节点
b = [0] * N
G1 = [[] for _ in range(N)] #邻接表
G2 = [[] for _ in range(N)]

def dfs(u1, far1, u2, far2, dep): ##far1和far2分别是u1和u2的父节点（用于避免回溯到父节点，从而避免形成环）
    global res
    res = max(res, dep)
    mp = {}
    for v in G1[u1]:
        if v == far1:
            continue
        mp[a[v]] = v ##为图G1中当前节点u1的所有邻居节点v（除了父节点far1）创建一个映射mp，将邻居节点的值映射到节点本身。
    for v in G2[u2]: ##对于每个这样的邻居节点v，检查G2中节点v的值是否在mp中存在。
        if v == far2:
            continue
        if b[v] in mp: ## 如果存在，说明找到了一个在两个图中对应值相同的节点对，于是递归调用dfs函数继续搜索
            dfs(mp[b[v]], u1, v, u2, dep + 1)


n, m = map(int, input().split())
res = 0
a[1:n+1] = map(int, input().split())
b[1:m+1] = map(int, input().split())
for _ in range(1, n):
    u, v = map(int, input().split())
    G1[u].append(v)
    G1[v].append(u)
for _ in range(1, m):
    u, v = map(int, input().split())
    G2[u].append(v)
    G2[v].append(u)

if a[1] != b[1]:
    print(0)
else:
    dfs(1, 0, 1, 0, 1)
    print(res)