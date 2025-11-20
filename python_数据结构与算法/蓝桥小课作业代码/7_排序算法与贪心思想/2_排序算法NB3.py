## 快速排序
dict1={1:0,2:0,3:0,4:1,5:0,6:1,7:0,8:2,9:1}
n=int(input())
lst1=list(input())
lst2=[]
for i in lst:
  if len(i)==1:
    if i in dict1:
      lst2.append(dict1[i])
  else:
    sum=0
    for j in i:
      if j in dict:
        j=dict[j]
        sum+=j
    lst2.append(sum)

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