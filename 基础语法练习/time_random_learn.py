import time

#返回本地时间元组
t1=time.localtime()
print(t1)

#日期格式化输出
t1=time.localtime()
t2=time.strftime("%Y-%m-%d %H:%M:%S",t1)
print(t2)

#读取当前时间并以易读方式表示，返回字符串
t5=time.ctime()
print(t5)

#获取当前时间戳
t3=time.time()
t4=int(t3)
print(t3)
print(t4)

#将指定时间转换为时间戳,strptime()将字符串对象转为时间日期对象，mktime()返回浮点数格式时间戳
time_str='2025-02-05 16:09:36'
timestamp=int(time.mktime(time.strptime(time_str,'%Y-%m-%d %H:%M:%S')))
print(timestamp)

#设置等待时长
time.sleep(3)




import random

#[0-1）内随机
a=random.random()
print(a)

#[a,b]内随机
a=random.randint(0,100)
print(a)

#随机从字符串、列表等对象中抽取一个元素
a=random.choice('abcdefg')
print(a)

#随机从字符串、列表等对象中抽取多个元素，且不重复
a=random.sample('abcdefg',3)
print(a)

#随机洗牌，比如打乱列表
list=[1,2,3,4,5,6]
random.shuffle(list)
print(list)


#日期时间的运算
from datetime import datetime,timedelta
t1=datetime.now()
print('开始时间：',t1)
delta_time=timedelta(hours=2,minutes=30) #设置增加时间：2小时30分钟
end_time=t1+delta_time
print('终止时间：',end_time)

#实时刷新
import time                                                                           
print("Loading",end = "")
for i in range(6):
    print(".",end = '',flush=True)
    time.sleep(2)