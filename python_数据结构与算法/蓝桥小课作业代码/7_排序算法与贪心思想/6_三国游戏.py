n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
p1=[a[i]-b[i]-c[i] for i in range(n)]
p2=[b[i]-a[i]-c[i] for i in range(n)]
p3=[c[i]-a[i]-b[i] for i in range(n)]
print(p1,p2,p3)
p1.sort(reverse=True)
p2.sort(reverse=True)
p3.sort(reverse=True)
print(p1,p2,p3)

sum1,sum2,sum3=0,0,0
count1,count2,count3=0,0,0
for i in range(n):
    sum1+=p1[i]
    if sum1<=0:
        count1=i
        if count1==0:
            count1=-1
            break
print(count1)

for i in range(n):
    sum2+=p2[i]
    if sum2<=0:
        count2=i
        if count2==0:
            count2=-1
            break
print(count2)

for i in range(n):
    sum3+=p3[i]
    if sum3<=0:
        count3=i
        if count3==0:
            count3=-1
            break
print(count3)

count=max(count1,count2,count3)
print(count)