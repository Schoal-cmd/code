#找零问题：贪心
#分数背包：贪心
goods=[(60,10),(100,20),(120,30)]
def fractional_backpack(goods,w):
    goods.sort(key=lambda x:x[0]/x[1],reverse=True)
    m=[0 for i in range(len(goods))] 
    total_value=0
    for i,(prize,weight) in enumerate(goods):
        #m[i]=1 if w>=weight else weight/w
        if w>=weight:
            m[i]=1
            w-=weight
            total_value+=prize
        else:
            m[i]=w/weight
            w=0
            total_value+=prize*m[i]
            break
    return m,total_value
print(fractional_backpack(goods,50))
#0-1背包:无法用贪心

#拼接最大数字问题
from functools import cmp_to_key

li=[32,94,128,1286,6,71]
def xy_cmp(x,y):
    if x+y<y+x:
        return 1 ##
    elif x+y>y+x:
        return -1
    else:
        return 0
    
def number_join(li):
    li=list(map(str,li))
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)

print(number_join(li))

#活动选择问题：贪心 找最早结束的活动
activities=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
##保证活动按结束时间排序
def activities_selection(activities):
    activities.sort(key=lambda x:x[1])
    m=[activities[0]]
    for i in range(1,len(activities)):
        if activities[i][0]>=m[-1][1]:
            m.append(activities[i])
    return m
print(activities_selection(activities))