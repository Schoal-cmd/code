import heapq
# 请在此输入您的代码
n=int(input())
heap=[]
for i in range(n):
  op=input().split()
  if op[0]=='push':
    x=int(op[1])
    heapq.heappush(heap,x)
  elif op[0]=='remove':
    if not heap:
      print('empty')
    else:
      heapq.heappop(heap)
  elif op[0]=='min':
    if not heap:
      print('empty')
    else:
      mini=heap[0]
      print(mini)
  elif op[0]=='print':
    k=int(op[1])
    num=[]
    for i in range(k):
      if not heap:
        continue
      a=heapq.heappop(heap)
      num.append(a)
    print(*num)