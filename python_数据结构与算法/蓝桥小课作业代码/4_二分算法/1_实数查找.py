#顺序查找    o（n）
## 在Python的for/else结构中，else子句只在for循环正常结束（即没有通过break语句提前退出）时才会执行。
## 在你的linear_search函数中，如果在循环中找到一个元素v == val，函数会通过return ind语句立即返回该元素的索引，并退出函数。这意味着循环会提前终止，不会继续执行到else子句。
def linear_search(lst,val):
    for ind,v in enumerate(lst):
        if v==val:
            return ind
    else:
        return None
seq = ['one', 'two', 'three']
print(linear_search(seq,'three'))


# 线性查找更常用，二分查找要先排序，虽然查找快，但要先排序花很多时间


# 二分查找  o（logn）
## 先排序;只能查找数字
## 候选区，无法删除，用指针维护候选区
## 只要有值：mid就可能等于这个值；没有值：right<left(循环条件)
### 注意写找不到值的返回情况
def binary_search(lst,val):
    left=0
    right=len(lst)-1
    while left<=right:
        mid=(left+right)//2
        if lst[mid]==val:
            return mid
        elif lst[mid]>val:
            right=mid-1
        elif lst[mid]<val:
            left=mid+1
    else:
        return None
lst=[1,2,3,4,5,6,7,8,9]
print(binary_search(lst,3))
lst=list(range(15))
print(lst)



import math
n = int(input())
cnt = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
vec = [[] for _ in range(21)]

x = list(map(int, input().split()))

for i in range(n):
    y = x[i]
    s = 0
    while y:
        s += cnt[y % 10]
        y //= 10
    vec[s].append(x[i])

for i in range(21):
    vec[i].sort()

for i in range(21):
    for j in vec[i]:
        print(j, end=" ")