##日期问题-年月日循环-datetime;闰年判断
##o(n**#3) 19ms
# 我的版本：
def practice():
    dict1 = {'0': 13, '1': 1, '2': 2, '3': 3, '4': 5, '5': 4, '6': 4, '7': 2, '8': 2, '9': 2}
    number = {1: '01', 2: '02', 3: '03', 4: '04', 5: '05', 6: '06', 7: '07', 8: '08', 9: '09'}
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = 0
    for y in range(2000,2025):
        if (y%4==0 and y%100!=0) or y%400==0:
            month[2]=29
        else:
            month[2]=28
        for m in range(1,13):
            for d in range(1,month[m]+1):
                if y==2024 and str(m)=='04' and d==14:
                    return ans
                total=0
                if m in number:
                    m=number[m]
                if d in number:
                    d=number[d]
                datetime=[str(y),str(m),str(d)]
                datetime=''.join(datetime)
                for i in datetime:
                    j=dict1[i]
                    total+=j
                if total>50:
                    ans+=1
print(practice())

# 使用datetime
import datetime
cur=datetime.datetime(2000,1,1)
ed=datetime.datetime(2024,4,13)
dict1={'0':13,'1':1,'2':2,'3':3,'4':5,'5':4,'6':4,'7':2,'8':2,'9':2}
count=0
while cur<=ed:
    j=0
    s=cur.strftime('%Y%m%d')
    for i in s:
        j+=dict1[i]
    if j>50:
        count+=1
    cur+=datetime.timedelta(days=1)
print(count)