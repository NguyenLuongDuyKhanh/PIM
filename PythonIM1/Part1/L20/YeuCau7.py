import turtle
import time
import random

game = True
collide = False
score = 0

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

score_points = turtle.Turtle()
score_points.pencolor("white")
score_points.fillcolor("white")
score_points.penup()
score_points.hideturtle()

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
    global score
    if ob.ycor() < -400:
        ob.setx(random.uniform(-200, 200))
        ob.sety(430)
        ob.dy = random.uniform(0.5, 0.7)
        score += 1
        score_points.clear()
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")

def check_collide(tur1, tur2):
    global collide
    if ((tur1.xcor() < (tur2.xcor() + 23)) and (tur1.xcor() > (tur2.xcor() - 23)) and (tur1.ycor() < (tur2.ycor() + 23)) and (tur1.ycor() > (tur2.ycor() - 23))):
        collide = True
    return collide

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

def retry():
    print("retry call")
    global game
    global collide
    global score
    game = True
    collide = False
    score = 0
    return game


s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.onkey(retry,"space")
s.listen()

S5GO()
tur.goto(0, -430)                               #after the countdown, the turtle should be back at the original location
obs.goto(0,400)
score_points.goto(-220, 430)
score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")
while game:
    if(obs.ycor() < -400):
        obs.hideturtle()
        rand_spot(obs)
        obs.showturtle()
    else:
        obs.sety(obs.ycor() - 10)
        check_collide(tur, obs)
        if collide == True:
            tur.write("Thua", font = ('', 72), align = "center")
            game = False
