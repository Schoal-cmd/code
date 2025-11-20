#模拟法
num=0
for i in range(0,50):
  for j in range(i+1,50):
    if i>6 or j>6:
      num+=1
print(num)

ans = 0
for i in range(1, 51):
  for j in range(i+1, 51):
    if i <= 7 and j <= 7:
      continue
    else:
      ans += 1
print(ans)

ans = 0
for i in range(1, 51):
  for j in range(i+1, 51):
    if j <= 7:
      continue
    else:
      ans += 1
print(ans)