import turtle
from turtle import Screen
import random
import time
a = 5
s = Screen()
s.setup(500,900)
s.bgcolor("black")
s.title("Vượt chướng ngại vật")

tina = turtle.Turtle()
tina.color("white")
tina.pu()
tina.goto(0,-300)
tina.lt(90)
tina.shape("turtle")

b = -10

obby = turtle.Turtle()
obby1 = turtle.Turtle()
obby2 = turtle.Turtle()
obby3 = turtle.Turtle()

obby.hideturtle()
obby1.hideturtle()
obby2.hideturtle()
obby3.hideturtle()

obby.penup()
obby.shape("square")
obby.color('red')
obby.penup()
obby.goto(random.randint(-200,200),300)
obby.rt(90)

obby1.penup()
obby1.shape("square")
obby1.color('red')
obby1.penup()
obby1.goto(random.randint(-200,200),300)
obby1.rt(90)

obby2.penup()
obby2.shape("square")
obby2.color('red')
obby2.penup()
obby2.goto(random.randint(-200,200),300)
obby2.rt(90)

obby3.penup()
obby3.shape("square")
obby3.color('red')
obby3.penup()
obby3.goto(random.randint(-200,200),300)
obby3.rt(90)

sodem = turtle.Turtle()
sodem.penup()
sodem.color("white")
sodem.goto(0,0)
for x in range(0,5):
    sodem.clear()
    sodem.write(str(a), font = ('',72), align = "center")
    a = a - 1
    time.sleep(1)
sodem.clear()
sodem.write("GO!", font = ('',72), align = "center")
time.sleep(1)
sodem.clear()
sodem.color("black")

obby.showturtle()
obby1.showturtle()
obby2.showturtle()
obby3.showturtle()

def move_up():
    if tina.ycor() < 430:
        tina.goto(tina.xcor(), tina.ycor() + 20)

def move_down():
    if tina.ycor() > -430:
        tina.goto(tina.xcor(), tina.ycor() - 20)

def move_right():
    if tina.xcor() < 190:
        tina.goto(tina.xcor() + 20, tina.ycor())

def move_left():
    if tina.xcor() > -190:
        tina.goto(tina.xcor() - 20, tina.ycor())

def randspot(obby):
    obby.goto(random.randint(-100,100), 300)

def spotrand(obby):
    obby.sety(obby.ycor() - 1)


s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")

s.listen()
game = True

def kiemtravacham(obby):
    global game
    if tina.ycor() >= obby.ycor() - 20 and tina.ycor() <= obby.ycor() + 20 and tina.xcor() >= obby.xcor() - 20 and tina.xcor() <= obby.xcor() + 20:
        tina.write("vacham")
        game = False
    else:
        tina.clear()

#Huy
s.tracer(0)

while game:
    s.update()
    if obby.ycor() < -430:
        randspot(obby)
        randspot(obby1)
        randspot(obby2)
        randspot(obby3)
    else:
        s.tracer()
        spotrand(obby)
        spotrand(obby1)
        spotrand(obby2)
        spotrand(obby3)
        kiemtravacham(obby)
        kiemtravacham(obby1)
        kiemtravacham(obby2)
        kiemtravacham(obby3)
        s.update()
