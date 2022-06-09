import turtle
from turtle import Screen
import time
import random

y = -200
x = 0

s = Screen()
s.setup(700, 700)
s.bgcolor("black")
s.title("hello python")

import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("blue")
tina.lt(90)
tina.pu()
tina.sety(-200)
rua = turtle.Turtle()
rua.ht()
rua.pu()
rua.lt(90)
rua.fd(150)
rua.color("red")
rua.write(str(5), font=("", 72), align="center")
time.sleep(1)
rua.clear()
rua.write(str(4), font=("", 72), align="center")
time.sleep(1)
rua.clear()
rua.write(str(3), font=("", 72), align="center")
time.sleep(1)
rua.clear()
rua.write(str(2), font=("", 72), align="center")
time.sleep(1)
rua.clear()
rua.write(str(1), font=("", 72), align="center")
time.sleep(1)
rua.clear()
rua.write(str("go"), font=("", 72), align="center")
time.sleep(1)
rua.clear()

chuongngaivat1 = turtle.Turtle()
chuongngaivat1.ht()
chuongngaivat1.shapesize(2,2)
chuongngaivat1.shape("triangle")
chuongngaivat1.color("red")
chuongngaivat1.pu()
chuongngaivat1.rt(90)
chuongngaivat1.goto(random.randint(50, 300), random.randint(50, 200))
chuongngaivat1.st()
chuongngaivat2 = turtle.Turtle()
chuongngaivat2.ht()
chuongngaivat2.shape("triangle")
chuongngaivat2.shapesize(2, 2)
chuongngaivat2.rt(90)
chuongngaivat2.color("red")
chuongngaivat2.pu()
chuongngaivat2.goto(random.randint(50, 300), random.randint(150, 200))
chuongngaivat2.st()
chuongngaivat3 = turtle.Turtle()
chuongngaivat3.ht()
chuongngaivat3.shapesize(2, 2)

chuongngaivat3.shape("triangle")
chuongngaivat3.rt(90)
chuongngaivat3.color("red")
chuongngaivat3.pu()
chuongngaivat3.goto(random.randint(50, 300), random.randint(50, 200))
chuongngaivat3.st()


def sangtrai():
    global x
    if x == -340 or x < -340:
        tina.setx(-320)
        x = -320
    if x > -340:
        x = x - 10
        tina.setx(x)


def sangphai():
    global x
    if x == 340 or x > 340:
        tina.setx(320)
        x = 320
    if x < 340:
        x = x + 10
        tina.setx(x)


def lentren():
    global y
    if y == 330:
        y = -200
        tina.sety(y)
    if y < 330:
        y = y + 10
        tina.sety(y)


def xuongduoi():
    global y
    if y < -300:
        tina.sety(-280)
        y = 280
    if y > -300:
        y = y - 10
        tina.sety(y)


def tha1():
    pass


def tha2():
    pass


def tha3():
    pass


def tha4():
    pass
def rand_spot(obs):
    goto(random.randint(50, 300), random.randint(50, 200))


s.onkeypress(xuongduoi, "Down")
s.onkeyrelease(tha1, "Down")
s.onkeypress(lentren, "Up")
s.onkeyrelease(tha2, "Up")
s.onkeypress(sangphai, "Right")
s.onkeyrelease(tha3, "Right")
s.onkeypress(sangtrai, "Left")
s.onkeyrelease(tha4, "Left")
s.listen()
s.tracer(0)

def kiemtravacham(chuongngaivat):
    if tina.ycor() >= chuongngaivat.ycor() - 20 and tina.ycor() <= chuongngaivat.ycor() + 20 and tina.xcor() >= chuongngaivat.xcor() -20 and tina.xcor() <= chuongngaivat.xcor() + 20:
        tina.write("vacham")
        print("vacham")
        break

while True:
    s.update()
    if chuongngaivat1.ycor() < -330:
        chuongngaivat1.goto(random.randint(50, 300), random.randint(50, 200))
    else:
        chuongngaivat1.sety(chuongngaivat1.ycor() - 0.5)
    kiemtravacham(chuongngaivat1)
    #kiemtravacham(chuongngaivat1)
    #print("tina",tina.pos(),"chuongngaivat1",chuongngaivat1.pos())
    time.sleep
    tina.clear()
# onkeypress
# onkeyrelease
# listen