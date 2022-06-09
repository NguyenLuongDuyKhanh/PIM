import turtle
import time
import random
# setting up screen
s = turtle.Screen()
s.setup(450, 900)
s.bgcolor("black")
s.title("turtle racing 2")


# tur is the main turtle to race
tur = turtle.Turtle()
tur.shape("turtle")
tur.penup()
tur.fillcolor("white")
tur.pencolor("blue")
tur.left(90)


tur.goto(0,-430)
tur.ondrag(tur.goto)

# obs is the obstacle
obs = turtle.Turtle()
obs.shape("square")
obs.shapesize(5, 5)
obs.penup()
obs.pencolor("red")
obs.fillcolor("red")


def move_up():
    if tur.ycor() < 430:
        tur.goto(tur.xcor(), tur.ycor() + 20)

def move_down():
    if tur.ycor() > -430:
        tur.goto(tur.xcor(), tur.ycor() - 20)

def move_right():
    if tur.xcor() < 190:
        tur.goto(tur.xcor() + 20, tur.ycor())

def move_left():
    if tur.xcor() > -190:
        tur.goto(tur.xcor() - 20, tur.ycor())

s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.listen()

tur.goto(0, -430)                               #after the countdown, the turtle should be back at the original location
obs.goto(0,0)

while True:
    if(tur.xcor() > obs.xcor() - 50 and tur.xcor() < obs.xcor() + 50 ):
        tur.write('va cham')
    else:
        tur.clear()
