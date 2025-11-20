import bisect

# 创建一个有序列表
a = [1,2,3,3,3,4,5]

# 使用bisect_left找到插入位置
index_left = bisect.bisect_left(a, 3)

# 使用bisect_right找到插入位置
index_right = bisect.bisect_right(a, 3)

# 输出插入位置
print(index_left) # 输出: 2
print(index_right) # 输出: 2



import bisect
arr=[5,2,7,9,2,7,0,2,66,7,34,7,5,23,67]
arr.sort(reverse=False)
print(arr)
n=len(arr)

greater=n-bisect.bisect_right(arr,5)
lower=bisect.bisect_left(arr,5)
print(greater,lower)