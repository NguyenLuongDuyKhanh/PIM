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
obs.shapesize(1.25, 1.25)
obs.penup()
obs.pencolor("red")
obs.fillcolor("red")


# cloning the first obstacle so we don't have to write this over again

# creating turtle and function to count down
CD = turtle.Turtle()
CD.penup()
CD.hideturtle()
CD.pencolor("white")
CD.fillcolor("white")
CD.goto(0, 100)


def S5GO():
    for i in range(5):
        CD.write(str(abs(5-i)), font = ('', 72), align = "center")
        time.sleep(1)
        CD.clear()
    CD.write("GO!", font=('', 72), align='center')
    time.sleep(.5)
    CD.clear()

def rand_spot(ob):
    if ob.ycor() < -400:
        ob.setx(random.uniform(-200, 200))
        ob.sety(430)
        ob.dy = random.uniform(0.5, 0.7)

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

S5GO()
tur.goto(0, -430)                               #after the countdown, the turtle should be back at the original location
obs.goto(0,400)
while True:
    if(obs.ycor() < -400):
        obs.hideturtle()
        rand_spot(obs)
        obs.showturtle()
    else:
        obs.sety(obs.ycor() - 10)
