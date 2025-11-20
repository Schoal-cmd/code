n=int(input())
mp={}
for i in range(n):
  arg=list(input().split())
  if arg[0]=='add':
    if (arg[1] not in mp) and (arg[2] not in mp):
      mp[arg[2]]=[arg[1]]
      print(mp)
    elif (arg[1] not in mp) and (arg[2] in mp):
      mp[arg[2]].append(arg[1])
      print(mp)
    else:
      continue
  else:
    if arg[1] not in mp:
      mp[arg[1]]=[]
    print(len(mp[arg[1]]))