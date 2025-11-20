### 趟                             共几趟
### 有序区 无序区                   范围




#冒泡排序  o(n**2)  最优情况o(n)
## 一趟，无序区最大的数升到最上面；不交换指针也会往上走
## 第i趟：无序区[0：n-i];指针到n-i-1
def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]: ##升序排列
                lst[j],lst[j+1]=lst[j+1],lst[j]
        ## print(lst)
    return lst

import random
lst=[random.randint(1,100) for i in range(10)]
print(lst)
bubble_sort(lst)
print(lst)
## 优化
def bubble_sort(lst):
    for i in range(len(lst)-1):
        exchange=False
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]: ##升序排列
                lst[j],lst[j+1]=lst[j+1],lst[j]
                exchange=True
        ## print(lst)
        if not exchange:
            break
    return lst
import random
lst=[1,2,3,4,5,6,7,8,9]
print(lst)
bubble_sort(lst)
print(lst)




#选择排序1.0
## 缺点：占内存；时间复杂度不止o(n),为o(n**2)
def select_sort_simple(lst):
    li=[]
    for i in range(len(lst)):
        mini=min(lst)
        li.append(mini)         ## 占用时间复杂的   
        lst.remove(mini)        ## 占用时间复杂的
    lst=li
    return lst
lst=[random.randint(1,10) for i in range(10)]
print(lst)
select_sort_simple(lst)
print(lst)

## o(n**2)
##优化：进行交换，找到的数和无序区第一个数交换
def select_sort(lst):
    ### 趟
    for i in range(len(lst)-1):
        ### 找
        mini=min(lst[i:len(lst)])
        ### 交换
        for ind in range(i,len(lst)):
            if lst[ind]==mini:
                lst[i],lst[ind]=lst[ind],lst[i]
    return lst
lst=[random.randint(1,10) for i in range(10)]
print(lst)
select_sort(lst)
print(lst)
##优化（不用min（）函数）：
def select_sort(lst):
    ### 趟
    for i in range(len(lst)):
        ### 找
        ind=i
        for j in range(i,len(lst)):
            if lst[j]<lst[ind]:
                ind=j
        ### 交换
        lst[i],lst[ind]=lst[ind],lst[i]
    return lst



#插入排序 o(n**2)
def insert_sort(lst):
    ###趟
    for i in range(1,len(lst)):
        j=i-1
        ### 取牌
        tmp=lst[i]
        ### 找插入位置
        while j>=0 and tmp<lst[j]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            j-=1
        ### 插入
        lst[j+1]=tmp
        ##print(lst)
    return lst
lst=[random.randint(1,10) for i in range(10)]
print(lst)
insert_sort(lst)
print(lst)