import csv

for i in dir(csv):
    print(i)

with open(r'D:\python\python练习代码\基础语法练习\csv文件操作\test.csv',newline='',encoding='utf-8') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)

with open(r'D:\python\python练习代码\基础语法练习\csv文件操作\test.csv','a',newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow([1,2,3,4,5])

