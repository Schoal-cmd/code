##回到起点说明小球水平方向移动的距离为长方形长度的偶数倍，小球在垂直方向上移动端距离为长方形宽度的偶数倍。
##7141ms
import math

def check(a,b):
    if a%b==0 and (a//b)%2==0:
        return True
    else:
        return False
t=1
x=343720
y=233333
while True:
    lx=15*t
    ly=17*t
    if check(lx,x) and check(ly,y):
        break
    t+=1

l=math.sqrt(lx**2+ly**2)
ll='{:.2f}'.format(l)
print(ll)