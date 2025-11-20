import turtle as t
import time

t.pensize(1)
t.pencolor('red')
t.fillcolor('pink')
t.speed(5)
t.up()
t.goto(-30, 100)
t.down()
t.begin_fill()
t.left(90)
t.circle(30,180)
t.circle(90,70)
t.left(38)
t.circle(90,70)
t.circle(30,180)
t.end_fill()

t.goto(30,100)
t.stamp()

time.sleep(3)