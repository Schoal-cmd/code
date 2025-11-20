import os
#linux系统
#os.system('ipconfig')

#windows系统-popen()
obj=os.popen('ipconfig')
print(obj)
print(obj.read())

#listdir(path)-列出指定目录下的所有文件和目录，包括隐藏文件，并以列表方式打印
lst=os.listdir()
print(lst)

print(os.listdir(r'D:\python\python练习代码\独角兽源代码'))

#getcwd()-获取当前工作目录
print(os.getcwd())
#获取当前python脚本的路径 + 文件名
print(__file__)
#返回绝对路径
print(os.path.abspath(__file__))

#返回文件名
print(os.path.basename(__file__))

# 判断路径是否为文件
print(os.path.isfile(__file__))
print(os.path.isfile(os.getcwd()))

# 判断路径是否为文件
print(os.path.isdir(__file__))

#os.mkdir(path)-创建文件夹
#os.mkdir(r'D:\python\python练习代码\基础语法练习\test.txt')

#chdir()-改变当前脚本工作目录；相当于shell下cd
#os.chdir(r'D:\python\python练习代码\基础语法练习\test.txt')

# 语法：os.replace(file1,file2)，将file1重命名为file2，将其替代。
os.replace(__file__, 'os_learn.py')  