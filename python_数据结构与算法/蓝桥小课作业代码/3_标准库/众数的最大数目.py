##关键思想：可以直接把元素三种操作后的值直接加入原列表，然后Counter计数找出最多的那个数；
## 因为从最后的结果来看，最多的那一种数，它要么没经过操作，要么+1得到，要么-1得到；
## 一个元素+1，-1一定得到不同的数，所以不存在重复计算的问题。

#法一
def main():
    mp = {}
    n = int(input())
    a = list(map(int, input().split()))

    for x in a:
        if x in mp:
            mp[x] += 1
        else:
            mp[x] = 1
        if x - 1 in mp:
            mp[x - 1] += 1
        else:
            mp[x - 1] = 1
        if x + 1 in mp:
            mp[x + 1] += 1
        else:
            mp[x + 1] = 1

    mx = 0
    for value in mp.values():
        mx = max(mx, value)

    print(mx)


if __name__ == "__main__":
    main()


#法二
from collections import Counter

n=int(input()) #3
a=list(map(int,input().split())) #1 2 3
for i in range(len(a)):
  a.append(a[i]-1)
  a.append(a[i]+1)
dic=Counter(a)
#print(dic)
#print(dic.most_common(1))
#print(dic.most_common(1)[0])
print(dic.most_common(1)[0][1])