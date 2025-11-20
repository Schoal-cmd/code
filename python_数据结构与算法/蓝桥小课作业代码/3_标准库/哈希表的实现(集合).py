s=set()
q=int(input())
for i in range(q):
  op,x=input().split()
  if op=='I':
    s.add(x)
  else:
    if x in s:
      print('Yes')
    else:
      print('No')