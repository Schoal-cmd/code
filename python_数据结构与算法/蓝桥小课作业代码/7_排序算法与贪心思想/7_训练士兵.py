
#要么全组团，要么全单独。除非你全单独训练比组团都便宜。
#看看全单独和组团谁便宜。要是组团还贵，以后每次训练都不用组团啦。因为再往后慢慢都顶尖了，费用包减少的。
try:
    n, s = map(int, input("请输入两个由空格分隔的整数: ").split(' '))
except ValueError as e:
    print(f"输入错误: {e}")
pc=[]
for i in range(n):
  p,c=map(int,input().split())
  pc.append([p,c])
pc.sort(key=lambda x:x[1],reverse=True)
### 找到临界士兵序号:逐一累加并比较大小
sump,count,ans=0,0,0
for i in range(n):
  sump+=pc[i][0]
  if sump>=s:
    count=i
    break
### 计算，分类求和
ans=pc[count][1]*s
for i in range(count):
  ans+=(pc[i][1]-pc[count][1])*pc[i][0] ###计算每个士兵开始单独训练后所需要的金币，在累加
print(ans)