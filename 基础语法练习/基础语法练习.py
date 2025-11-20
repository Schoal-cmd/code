###file=open("D:\\python练习代码\\try.txt",'r')


#调用模块--import 模块名
import time
import random
#time模块
##延时函数
time.sleep(1.5)
#random模块
##生成随机一个数字
a=random.randint(5,10)
print(a)
time.sleep(1)
##从列表或字典中随机抽取一个元素
canteens=['荷园','芷园','稻香园','莘园',"西园"]
scores={'firstterm':4.0,'secondterm':4.1,'thirdterm':4.2}
a=random.choice(canteens)
print(a)

#输出函数print()
print('你好，编程世界')
print("hello,let's go!")
print(237+111)
#换行
print('''你好，
python编程世界
我 鱼群 杀回来啦！''')
print('你好，\npython编程世界，\n我 鱼群 杀回来啦！')
##实现一次换两行
print('\n')
#print不换行：end参数
print('你好',end='')
print('编程世界')
print('你好',end=' ')
print('编程世界')
print('你好',end=' ! ')
print('编程世界')
#转义字符
#print('Let's go') 报错
print('Let\'s go!')
#变量与赋值
##变量只能有字母、数字、下划线，不能以数字开头
## =表示赋值，==表逻辑上的等于
name="鱼鱼鱼鱼群"
name='HaoDUoYu'
print(name)

#三种数据类型
print("字符串str：被引号括起来的文本。")
print("整数integer：int没有小数点的数，是正整数、负整数和零的统称。\n无需引号，可进行计算。")
print("浮点数：无简写，带小数点的数。")
##运算顺序同日常计算，先加减后乘除，有括号先算括号。
## +加 -减 *乘 /除
integer1=5-4
integer2=2*3
float3=8/2
print(integer1)
print(integer2)
print(float3)
## **幂-2**3-2的3次方，%取模-返回除法的余数，//取整数-返回商的整数部分
#查询数据类型-type()函数
result=type("你好，编程世界")
print(result)
print(type(name))
print(type(integer1))
print(type(float3))
a=8//2
b=8.0//2.0
print(type(a))
print(a)
print(type(b))
print(b)

#布尔值
## True：判断为真；False：判断为假
##布尔运算：逻辑判断
print(3<5)
print(3>5)
print('鱼群'=='鱼群')
print('鱼群'!='俞群')
##布尔值之间的运算
print(bool(not True))
print(bool(not False))
print(bool(True and True))
print(bool(False and False))
print(bool(True and False)) ### False
print(bool(True or True))
print(bool(False or False))
print(bool(True or False)) ### True
##查询数据布尔值-bool()函数
print(bool(False))
print(bool(0))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(None))
###就这些为假，其他的都为真！


#数据拼接
##数据拼接符号‘+’
##变量内的数据为字符串时拼接，为int或float时表运算；只能字符串和字符串凭借，数字和数字计算
print(integer1+integer2)
print('你好，欢迎回来'+name+'女士')
print('\n你好，欢迎回来！\n美丽的'+name+'女士')
welcome='\n你好，欢迎回来！\n美丽的'
print(welcome+name+'女士')
### name=111
### print('你好，欢迎回来'+name+'女士')   依然会报错
##运用逗号
print('\n你好，欢迎回来！\n美丽的',name,'女士')
name=111
print('\n你好，欢迎回来！\n美丽的',name,'女士')
##格式符%--%s、%d、%f--先占一个位置，之后再填上实际的变量
print('\n你好，欢迎回来！\n美丽的%d女士'%(111))
print('\n今天是%d年%d月%d日'%(2024,11,3))
##format()函数
print('\n你好，欢迎回来。美丽的{}女士'.format(111))
print('\n今天是{}年{}月{}日'.format (2024,11,3))

#数据类型转换
##转换为字符串类型：直接加引号；str()函数
result=type(integer1)
print(result)
result=type(str(integer1))
print(result)
integer1=str(integer1)
print(type(integer1))
## int()函数，字符串只有符合整数规范的才能转换，浮点数则回强制转换（浮点数时保留整数部分而不是四舍五入！！）
a='5'
b='7.0'
c=7.6
a=int(a)
### b=int(b) 报错，无法转换
c=int(c)
print(type(a))
### print(type(b)) 报错，转换不成功
print(type(c)) 
print(c)
## float()函数，整数✔，字符串则内含数据只需为数字形式
a='5'
b='7.0'
c=76
a=float(a)
b=float(b)
c=float(c)
print(a)
print(b)
print(c)

# 输入函数input()
##括号里面的内容会被打印出来；需要输入对应的内容回车后才能继续；
##输出结果需要赋值给变量；输出结果数据类型为字符串型
input("请输入您的用户名：")
name=input("请输入您的用户名")
#input()函数的数据类型转换
##用int()、float()从源头转换数据类型，但要求此时输入值必须是纯数字型！！！
grades=float(input("你的目标期末绩点是多少？"))
print(type(grades))

#条件判断和条件嵌套
#条件判断
##单向判断：
name=input("请输入您的用户名：")
if name=="凌羊心":
    print("主人，我等你等了一万年，你终于踏着七彩祥云回来见我了QAQ")
##双向判断：
if name=="凌羊心":
    print("主人，我等你等了一万年，你终于踏着七彩祥云来见我了QAQ")
else:
    print("Authentication Failed")
##多向判断：
if name=="凌羊心":
    print("主人，我等你等了一万年，你终于踏着七彩祥云来见我了QAQ")
elif name=="鱼鱼鱼鱼群":
    print("主人！欢迎你变强归来！让我们一起进击python编程世界！Fighting~~！")
elif name=="HaoDUoYu":
    print('\n你好，欢迎回来！\n美丽的'+name+'女士\n让我们重新征战编程世界！')
else:
    print("Authentication Failed")
###记得在判断前先对变量进行赋值，注意缩进关系，==连等号表逻辑判断，：英文冒号不能漏
#if嵌套
Finalgradepoint=4.2
if Finalgradepoint>=4.0:
    print("你很优秀")
    if Finalgradepoint>=4.5:
        print("你已经是站在本学期金字塔顶尖的一部分人啦")
    else:
        print("只要持之以恒，坚持不懈，你一定会更上一层楼")
else:
    print("没达到目标")
    if Finalgradepoint<=3.0:
        print("学渣")
    else:
        print("你是不是偷懒了")

#列表和字典
##列表：中括号；元素自成一体，元素之间都用逗号隔开；    有序性-偏移量；
##字典：大括号；键值对-键有唯一性而值可重复-用冒号赋值；无序性-用键定位。
###列表中，双引号可以用但最终同单引号
#列表-提取元素
##偏移量：元素在列表中从0开始的编号
canteens=['荷园','芷园','稻香园','莘园',"西园"]
canteen=['荷园一楼','荷园二楼','荷园三楼']
appetizer=['培根石锅拌饭','石锅鸡蛋','蛋包饭','鱼香肉丝小面']
print(canteens[0])
print(canteens[3])
###可用偏移量提取单个元素，结果为元素本身
##切片：用冒号来截取列表元素的操作
print(canteen[:3]) 
print(canteen[0:3]) ###冒号左边为0或空，:m ，都表示从头取m个元素
print(appetizer[2:])
print(appetizer[2:0]) ### n:0,表示跳过前面n个元素把剩下的取完
print(appetizer[1:4]) ### n:m 跳过前n个，取到第m个（取出前m个中除掉前n个的部分）
###这里的n、m都表示取几个元素，而不从偏移量的角度理解
###切片是截取列表的列表的一部分，所以结果仍未列表
##同时赋值
###当变量数与列表元素！个数一致！时，列表元素会一一赋值给变量
###提取结果为单个元素、元素本身
a,b,c,d,e=canteens
print(a)
print(b)
print(a,b,c,d,e)

#列表-增加元素
##列表名.append()函数--在列表  ！末尾！新增 ！一个！ 元素；！中间.连接
canteens.append('竹铭餐厅')
canteens.append("酸奶文创馆")
canteens.append(canteen)
print(canteens)
f=canteens.append('其他')
print(f) ##结果只有None
#列表-删除元素
##del 列表名[元素的索引]--能删除单个元素、多个元素（切片）、整个列表；！中间空格连接
del canteens[7]
print(canteens)
del canteens[5:7]
print(canteens)
del canteens[5:]
print(canteens)
## .pop()函数--可指定参数，或默认删除最后一个元素，并返回该元素
canteens.append('其他食堂')
others=canteens.pop(5)
print(others)
#列表-修改元素：用偏移量修改对应位置
appetizer[0]='韩式五彩拌饭'
print(appetizer)
#字典-提取
##字典名[字典的键]：提取出的是对应的value，而不会显示key
### scores={firstterm:4.0} key没用引号，回报错
scores={'firstterm':4.0,'secondterm':4.1,'thirdterm':4.2}
print(scores)
print(scores['thirdterm'])
print(scores["firstterm"])
#字典-增元删改查
##字典名[键]=值--每次只能增加一个键值对，否则报错；del
#嵌套
##字典与字典：字典中存储了两个字典，所以提取数据时只能用key值。
score={'第一组':{'小明':95,'小红':96},'第二组':{'小刚':94,'小青':99}}
print(score['第一组']['小红'])
##列表与字典：使用偏移量从最外层括号到最内层括号取数。
townee = [{'海底王国':['小美人鱼''海之王''小美人鱼的祖母''五位姐姐'],'上层世界':['王子','邻国公主']},'丑小鸭','坚定的锡兵','睡美人','青蛙王子',[{'主角':'小红帽','配角1':'外婆','配角2':'猎人'},{'反面角色':'狼'}]]
###想取出“狼”
print(townee[5][1]['反面角色'])
#获取列表和字典的元素数量
##len()函数

#range()函数
##range(m,n,p)--n>m，生成m到n-1中间隔为p的整数序列；取头不取尾
for i in range(5):
    print(i)
for i in range(0,5):
    print(i)
for i in range(1,7):
    print(i)
for i in range(1,15,2):
    print(i)
#for...in...循环
for i in "鱼鱼鱼鱼群":
    print(i)
for i in canteens:
    print(i)
for i in scores:
    print(i)
for i in scores:
    print(scores[i])
for i in range(3):
    print('鱼鱼鱼鱼群')
#while循环
a=0 ##循环前必须要定义变量
b=2
while a<5:
    print(a)
    a=a+1  ##为避免陷入死循环，循环内要更新变量
###循环次数明确：for循环；循环次数不明确：while循环

#break语句--如果满足了某一个条件，就提前结束循环
# 只能在循环内部使用！！--break前的缩进Tab键和空格键不能同时混用！！！
#for...in...:
#    ...
#    if ...:
#        break
#while...(条件):
#    ...
#    if ...:
#        break

#continue语句
# 在循环内部使用，当条件满足时，触发continue语句，将跳过之后的代码，直接回到循环的开始，即结束本次循环，开启下次循环。

#pass语句
# 常与if配合使用。为了保持代码结构的完整性，pass不做任何操作，只是充当了一个占位语句。
# 当没想好结构中具体的代码时，可以先用pass占位，保证程序正常运行不报错。

#else语句
# 当循环中没有碰到break语句、continue语句等跳出循环的操作时，就会执行循环后面的else语句，否则就不会执行。

#元组tuple
## 写法是把数据放在小括号()中，它的用法和列表用法类似，
## 主要区别在于列表中的元素可以随时修改，但元组中的元素不可更改。列表一样，元组是可迭代对象，这意味着我们可以用for循环来遍历它

#函数
#函数参数
## 位置参数：参数顺序和个数要和函数定义中一一对应；
## 默认参数：位于位置参数之后，调用函数时没有传递参数则为默认值
## 不定长参数：【*参数名】传入此处的参数数量不确定，数据类型为元组
def  menu(appetizer,course,dessert='绿豆沙'):
    print('一份开胃菜：'+appetizer)
    print('一份主食：'+course)
    print('一份甜品：'+dessert)
menu('话梅花生','牛肉拉面')
#结果显示为：因为调用时只给了两个参数，第三个参数为默认值
menu('话梅花生','牛肉拉面','银耳羹')
#结果显示为：因为调用时给了三个参数，第三个参数被更新
###- 当默认参数在不定长参数后时，若想更改默认参数，需要注明dessert='银耳羹'，例如：
def menu(appetizer,course,*barbeque,dessert='绿豆沙'):
    print('一份开胃菜：'+appetizer)
    print('一份主菜：'+course)
    print('一份甜品：'+dessert)
    for i in barbeque:
        print('一份烤串：'+i)  
menu('话梅花生','牛肉拉面','烤鸡翅','烤茄子','烤玉米',dessert='银耳羹')
###当默认参数在不定长参数之前，则默认按顺序传递参数（默认参数会改变），剩下的参数均传递给不定长参数
def menu(appetizer,course,dessert='绿豆沙',*barbeque):
    print('一份开胃菜：'+appetizer)
    print('一份主菜：'+course)
    print('一份甜品：'+dessert)
    for i in barbeque:
        print('一份烤串：'+i)     
menu('话梅花生','牛肉拉面','银耳羹','烤鸡翅','烤茄子','烤玉米')
#定义函数
##def 函数名(参数1，参数2，...参数n)：
##函数体
# return 语句
## 函数内部一旦遇到return语句，就会停止执行并返回结果。
## 没有return语句的函数，Python也会在末尾隐性地加上return None，即返回None值（return None可以简写为return。）
## 如果不是立即要对函数返回值做操作，可以用return语句保留返回值。
## 需要多次调用函数时，可以定义一个主函数main()，调用非主函数的返回值。
def face(name):
    return name + '的脸蛋'
def body(name):
    return name + '的身材'
def main(dream_face,dream_body):
    return '我的梦中情人：' + face(dream_face) + ' + ' + body(dream_body)
print(main('祁煜','秦彻'))
### 若需要返回多个值，在return后用逗号隔开即可，此时返回的是一个元组。
def lover(name1,name2):
    face= name1 + '的脸蛋'
    body= name2 + '的身材'
    return face,body
a=lover('夏以昼','黎深')
#此时return的值为元组 ('李若彤的脸蛋', '林志玲的身材')，并赋值给变量 a 。
print('我的梦中情人：'+a[0]+' + '+a[1])
#变量的作用域：局部变量、全局变量
##全局变量在函数内仍有效
##global语句
def egg():
    global quantity
#global语句将变量quantity声明为全局变量
    quantity = 108
egg()
print(quantity)
#函数的嵌套
rent=3000
def cost():
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本是' + str(variable_cost))
    return variable_cost
def sum_cost():
    sum = rent + cost()#调用函数
    print('本月的总成本是' + str(sum))
##sum = rent + cost() 的结果就是sum = rent + variable_cost（cost()函数的返回值）。最后调用函数时，也只需调用sum_cost()即可。
sum_cost()

#其他函数
#list()将数据转换为列表
a=list((1,2,3,4,5))
print(a)
#extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
##如果extend的是字符串，则字符串会被拆分成字符数组，如果extend的是字典，则字典的key会被加入到ist中。
canteens[0]=canteen
print(canteens)
canteens.pop(0)
print(canteens)
canteens.extend(canteen)
print(canteens)
canteens=['荷园','芷园','稻香园','莘园',"西园"]
canteen=['荷园一楼','荷园二楼','荷园三楼']
appetizer=['培根石锅拌饭','石锅鸡蛋','蛋包饭','鱼香肉丝小面']

#类与对象
num1 = [1,2,3,4,5] # 想一想，如果用这个方法生成一个1-100的列表……
num2 = list(range(1,6))
print(num1)
print(num2)

# 知识点3：列表生成式
list1 = [i for i in range(3)] # 规定列表中元素的范围
print(list1)
list2 = [m+n for m in ['天字', '地字'] for n in '一二']# 列表元素可以是组合，分别规定范围。
print(list2)
list3 = [n*n for n in range(1,11) if n % 3 == 0] # 元素既可规定范围，也可附加条件。
print(list3)