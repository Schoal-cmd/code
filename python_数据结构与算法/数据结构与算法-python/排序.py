import copy
import sys #用于修改递归最大深度
sys.setrecursionlimit(100000)

#时间复杂度-时间装饰器
import time
def cal_time(func):
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=func(*args,**kwargs)
        t2=time.time()
        print('%s running time: %s secs.'%(func.__name__,t2-t1))
    return wrapper

#查找
a=[1,2,3,4,5,6,]
b=list(range(1000000))
#顺序查找
#时间复杂度O(n)

def linear_search(li,val):
    for ind,v in enumerate(li):
        if v == val:
            return ind
    else:
        return None

ind=linear_search(a,6)
print('经查找，目标元素在列表内的索引号为%s'%(ind))

linear_search(b,366000)

#二分查找
#只能用于查找数据
#时间复杂度：O(logn)
@cal_time
def binary_search(li,val):
    li.sort()
    left=0
    right=len(li)-1
    while left<=right:
        mid=(left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val:
            right=mid-1
        else:
            left=mid+1
    else:
        return None

ind=binary_search(a,3)
print('经查找，目标元素在列表内的索引号为%s'%(ind))

binary_search(b,366000)

#生成无需列表
import random
a=list(range(20))
print(a)
random.shuffle(a)
print('列表a:',a)

b=list(random.randint(0,20) for i in range(10))
print('列表b：',b)

#冒泡排序（升序）
#时间复杂度O(n**2)
def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li

print('冒泡排序：',bubble_sort(a))
print('冒泡排序：',bubble_sort(b))

#冒泡排序2.0
def bubble_sort(li):
    for i in range(len(li)):
        exchange=True
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=False
        if exchange:
            break
    return li

a=[7,8,9,1,2,3,4,5,6]
print('列表a:',a)
print('冒泡排序2.0：',bubble_sort(a))

#选择排序1.0
#新建了一个列表，占用两倍内存 VS原地排序
#o(n**2)
def select_sort(lst):
    lst_new=[]
    for i in range(len(lst)): #O(n)
        mini=min(lst) #O(n)
        lst_new.append(mini)
        lst.remove(mini) #O(n)
    return lst_new

#选择排序2.0
#找到最小的数和列表头无序区第一个数交换 o(n**2)
#我写的：
def select_sort(lst):
    for i in range(len(lst)-1):
        mini=min(lst[i:len(lst)])
        ind=linear_search(lst, mini)
        lst[ind],lst[i]=lst[i],lst[ind]
    return lst   
b=list(random.randint(0,20) for i in range(10))
print('列表b：',b) 
print('选择排序：',select_sort(b))
#标准的(更好)：
def select_sort(lst):
    for i in range(len(lst)-1):
        ind=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[i]:
                ind=j
        lst[ind],lst[i]=lst[i],lst[ind]
    return lst
b=list(random.randint(0,20) for i in range(10))
print('列表b：',b)
print('选择排序：',select_sort(b))

#插入排序 o(n**2)
##原地排序要从右往左进行，不然前一个元素没位置交换
def insert_sort(lst):
    for i in range(1,len(lst)):
        ind=i-1
        while ind>=0 and lst[ind]>lst[i]:
            lst[ind],lst[i]=lst[i],lst[ind]
            ind=ind-1
    return lst
b=list(random.randint(0,20) for i in range(10))
print('列表b：',b)
print('插入排序：',insert_sort(b))
#写法2
def insert_sort(lst):
    for i in range(1,len(lst)):
        temp=lst[i]
        j=i-1
        while j>=0 and lst[j]>temp:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=temp
    return lst
b=list(random.randint(0,20) for i in range(10))
print('列表b：',b)
print('插入排序：',insert_sort(b))

#快速排序：P归位+递归 o(n*logn)
#左右横跳算法/挖坑填坑法
#p归位
def partition(lst,left,right):
    temp=lst[left]
    while left<right:
        while left<right and lst[right]>=temp:
            right-=1
        lst[left]=lst[right]
        while left<right and lst[left]<=temp:
            left+=1
        lst[right]=lst[left]
    lst[left]=temp
    return left
b=list(random.randint(0,20) for i in range(10))
print('列表b：',b)
print(partition(b,0,len(b)-1))
print('p归位后：',b)

def _quick_sort(lst,left,right):
    if left<right:
        mid=partition(lst,left,right)
        _quick_sort(lst,left,mid-1)
        _quick_sort(lst,mid+1,right)
    return lst

@cal_time
def quick_sort(lst):
    _quick_sort(lst,0,len(lst)-1)

b=list(range(1000))
random.shuffle(b)
print('快速排序：',quick_sort(b))
#递归最大深度：999
#一定程度消耗系统资源
#最坏情况：最坏时间复杂度 o（n**2）
lst=list(range(1000,0,-1))
print('快速排序最坏情况：',quick_sort(lst))
#解决办法：加入随机化


#归并
def merge(lst,low,mid,high):
    i=low
    j=mid+1
    li=[]
    while i<=mid and j<=high:
        if lst[i]<=lst[j]:
            li.append(lst[i])
            i+=1
        else:
            li.append(lst[j])
            j+=1
    while j<=high:
        li.append(lst[j])
        j+=1
    while i<=mid:
        li.append(lst[i])
        i+=1
    lst[low:high+1]=li
#归并排序
def merge_sort(lst,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(lst,low,mid)
        merge_sort(lst,mid+1,high)
        #print(lst[low:high+1])
        merge(lst,low,mid,high)
b=list(random.randint(0,20) for i in range(10))
#b=[1,3,4,6,2,5,7,9]
print('列表b：',b)
merge_sort(b,0,len(b)-1)
print('归并排序：',b)
print(b)