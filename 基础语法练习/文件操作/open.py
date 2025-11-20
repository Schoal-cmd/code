#编码和解码
print('俞群'.encode('gbk'))
print('俞群'.encode('utf-8'))

print(b'\xd3\xe1\xc8\xba'.decode('gbk'))
print(b'\xe4\xbf\x9e\xe7\xbe\xa4'.decode('utf-8'))
print('')
#读取文件
file1=open(r'D:\python\python小课作业代码\基础语法练习\test\abc.txt','r',encoding='utf-8')
filecontent=file1.read()
print(filecontent)
file1.close()

#写入文件
file=open(r'D:\python\python小课作业代码\基础语法练习\test\abc.txt','w+',encoding='utf-8')
file.write('祁煜\n')
file.write('黎深\n')
file.write('秦彻\n')
file.close()

#追加写入文件
file=open(r'python小课作业代码\基础语法练习\test\abc.txt','a',encoding='utf-8')
file.write('夏以昼\n')
file.write('沈星回\n')
file.close()

#读取文件
file1=open(r'D:\python\python小课作业代码\基础语法练习\test\abc.txt','r',encoding='utf-8')
filecontent=file1.read()
print(filecontent)
file1.close()

#按行读取
file=open(r'python小课作业代码\基础语法练习\test\score.txt','r',encoding='utf-8')
file_lines=file.readlines()
file.close()
print(file_lines)

for i in file_lines:
    print(i)

for i in file_lines:
    data=i.split()
    print(data)

# 用for...in...循环进行加法的操作
final_scores=[]
for i in file_lines:
    data=i.split()
    sum=0
    for score in data[1:]:
        sum=sum+int(score)
    result=data[0]+str(sum)+'\n'
    print(result)
    final_scores.append(result)

#按行写入
print(final_scores)
new_file=open(r'D:\python\python小课作业代码\基础语法练习\test\final_scores.txt','w',encoding='utf-8')
new_file.writelines(final_scores)
new_file.close()

#读取 photo1 里的数据
with open(r'D:\python\python小课作业代码\基础语法练习\test\photo1.png','rb') as file1:
    filecontent=file1.read()

#将photo1的数据写入photo2
with open(r'D:\python\python小课作业代码\基础语法练习\test\photo2.png','wb') as file2:
    file2.write(filecontent)

#让学员的成绩从高到低排列，然后放到新文档
print('new start')
with open(r'python小课作业代码\基础语法练习\test\final_scores.txt','r',encoding='utf-8') as file:
    file_lines=file.readlines()

dict_scores_name={}
list_scores=[]
final_scores=[]

print(file_lines)
print(len('\n'))

for i in file_lines:
    name=i[:-4]
    score=i[-4:-1]
    dict_scores_name[score]=name
    list_scores.append(score)

print(dict_scores_name)
print(list_scores)
list_scores.sort(reverse=True)
print(list_scores)

for i in list_scores:
    result=dict_scores_name[i]+str(i)+'\n'
    print(result)
    final_scores.append(result)
print(final_scores)

with open(r'D:\python\python小课作业代码\基础语法练习\test\new_final_scores.txt','w',encoding='utf-8') as file:
    file.writelines(final_scores)

#直接修改原文件中的数据-故事默写1.0
list_test = ['一弦一柱思华年。\n','只是当时已惘然。']  # 将要默写的诗句放在列表里。
with open (r'python小课作业代码\基础语法练习\test\poem.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
with open(r'python小课作业代码\基础语法练习\test\poem.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)

#直接修改原文件中的数据-故事默写2.0
import os

list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']

with open ('poem.txt','r') as f:
    lines = f.readlines()

with open('poem_new.txt','w') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

os.replace('poem_new.txt', 'poem3.txt')