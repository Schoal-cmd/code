##打印汉诺塔过程
##将上面n-1个盘子当作一个整体，最下面一个盘子，抽象成两个盘子的汉诺塔移动过程。
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s"%(a,c))  ###这一步是对第n个盘子的操作
        hanoi(n-1,b,a,c)
hanoi(4,'A','B','C')


##n表示要移动的盘子个数，m表示最少移动步数的第m步，要求表示出第m步是什么；盘子编号从上到下依次从1到n
###因为ans是全局变量，所以在递归中不同函数中计数保持连贯
ans=0
n,m=map(int,input().split())
def hanoi_1(n,a,b,c):
    global ans,m
    if n>0:
        hanoi_1(n-1,a,c,b)
        ans+=1
        if ans==m:
            print("#%s: %s->%s"%(n,a,c))
        hanoi_1(n-1,b,a,c)
    return ans
print(hanoi_1(n,'A','B','C'))

