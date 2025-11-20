count=0
left=0
right=len(mp)-1
def check(mid):
  cent=0
  for i in lst[0,mid+1]:
    if mp[i]!=mp[i+1]:
      cent+=1
  return cent


def binary_search(lst,k):
  while left<=right:
    mid=(left+right)//2
    k_=check(lst,mid)
    if k_==k-1:
      print(lst[mid])
      break
    elif k_>k-1:
      right=mid-1
    elif k_<k-1:
      left=mid+1
  else:
    return None