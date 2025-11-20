#莲东中学 八4班 俞群 参赛作品：
# 带翅膀的独角兽
#独角兽形象来源于网络，代码为自己编写：

import turtle as t
import time

t.screensize(100,200)
t.color=('black','yellow','red','pink','blue')
t.pensize(2)
t.bgpic(r'F:\\PPT\\ppt素材图片\\背景.gif')

#开始
t.up()
t.goto(-280,230)
t.write("你梦中是否有这样一个独角兽:", font=("Arial", 14, "bold"))

#大大的顺风耳
t.penup()
t.goto(30,40)
t.left(70)
t.pendown()
t.circle(20,180)

#开开爱爱的脑袋
t.right(70)
t.fd(20)

t.circle(30,180)
t.fd(20)

#肥嘟嘟滴身子
t.penup()
t.left(180)
t.fd(20)
t.left(80)
t.pendown()
t.fd(40)

t.penup()
t.goto(30,40)
t.left(25)
t.pendown()
t.fd(100)

#萌萌滴内耳
t.begin_fill()
t.penup()
t.fillcolor("#FFF0F5")
t.goto(20,45)
t.right(210)
t.pendown()
t.circle(10,180)
t.left(90)
t.fd(20)
t.end_fill()

#独角兽的角
t.begin_fill()
t.fillcolor("#F9E580")
t.penup()
t.goto(-20,54)
t.left(120)
t.pendown()
t.fd(29)
t.left(160)
t.fd(29)
t.end_fill()

#可爱滴眼睛
t.begin_fill()
t.fillcolor("#696969")
t.penup()
t.goto(-35,30)
t.pendown()
t.circle(5,180)
t.left(5)
t.fd(10)
t.circle(5,180)
t.fd(10)
t.end_fill()

t.begin_fill()
t.fillcolor("black")
t.penup()
t.goto(-35,35)
t.pendown()
t.circle(3)
t.end_fill()

#秀丽的鬃毛
t.penup()
t.goto(-10,65)
t.right(90)
t.pendown()
t.circle(10,90)

t.penup()
t.goto(42,38)
t.left(155)
t.pendown()
t.circle(30,180)

t.penup()
t.goto(55,0)
t.left(135)
t.pendown()
t.circle(20,180)

t.penup()
t.goto(75,-50)
t.left(195)
t.pendown()
t.circle(30,150)


#美丽滴翅膀
t.fillcolor("#F9E580")
t.begin_fill()
t.penup()
t.goto(60,0)
t.left(190)
t.pendown()
t.circle(8,180)
t.circle(15,180)
t.fd(20)
t.circle(6,180)
t.fd(5)
t.left(180)
t.fd(10)
t.circle(7,180)
t.fd(10)
t.left(180)
t.fd(20)
t.circle(8,180)
t.fd(40)
t.circle(20,180)
t.fd(3)
t.end_fill()

#手来也~
t.begin_fill()
t.fillcolor("#FFF0F5")
t.up()
t.goto(-45,-30)
t.left(150)
t.down()
t.fd(10)
t.circle(8,180)
t.fd(10)
t.end_fill()

t.begin_fill()
t.fillcolor("#FFF0F5")
t.up()
t.goto(0,-40)
t.left(150)
t.down()
t.fd(10)
t.circle(8,180)
t.fd(10)
t.end_fill()

#手捧爱心
t.pencolor('red')
t.fillcolor('pink')
t.speed(5)
t.up()
t.goto(-100, 0)
t.down()
t.begin_fill()
t.left(90)
t.circle(15,180)
t.circle(45,70)
t.left(38)
t.circle(45,70)
t.circle(15,180)
t.end_fill()

#署名
t.up()
t.goto(-50,-280)
t.write("发挥想象成就自己心里的独角兽~", font=("Arial", 14, "bold"))
time.sleep(1)
t.goto(50,50)
t.write("Cody by 俞群", font=("Arial", 14, "bold"))
#完成~
time.sleep(3)
