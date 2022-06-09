# Write your code here :-)
import turtle
import time
import random
from turtle import Screen
screen = Screen()
screen.colormode(255)
game = True
lose = False
collide = False
score = 0
high_score = 0

# setting up screen
s = turtle.Screen()
s.setup(450, 700)
s.bgcolor((random.randint(0,90),random.randint(0,90),random.randint(0,90)))
s.title("turtle racing 2")
s.tracer(0)


# tur is the main turtle to race
tur = turtle.Turtle()
tur.shape("turtle")
tur.penup()

tur.left(90)
tur.color('yellow')

tur.goto(0,-320)
tur.ondrag(tur.goto)


# obs is the obstacle
obs = turtle.Turtle()
obs.shape("turtle")
obs.shapesize(1.25, 1.25)
obs.penup()
obs.right(90)



# cloning the first obstacle so we don't have to write this over again

obs1 = obs.clone()
obs2 = obs.clone()
obs3 = obs.clone()
obs4 = obs.clone()
obs5 = obs.clone()
obs.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
obs1.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
obs2.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
obs3.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
obs4.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
obs5.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# creating score, high score turtle
score_points = turtle.Turtle()
score_points.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
score_points.fillcolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
score_points.penup()
score_points.hideturtle()

high_score_points = turtle.Turtle()
high_score_points.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
high_score_points.fillcolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
high_score_points.penup()
high_score_points.hideturtle()


# creating turtle and function to count down
CD = turtle.Turtle()
CD.penup()
CD.hideturtle()
CD.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
CD.fillcolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
CD.goto(0, 100)


def S5GO():
    for i in range(5):
        CD.write(str(abs(5-i)), font = ('', 72), align = "center")
        time.sleep(1)
        CD.clear()
    CD.write("GO!", font=('', 72), align='center')
    time.sleep(.5)
    CD.clear()


GO = turtle.Turtle()
GO.penup()
GO.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
GO.fillcolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
GO.hideturtle()
GO.goto(0, 100)
PSR = turtle.Turtle()
PSR.penup()
PSR.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
PSR.fillcolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
PSR.hideturtle()
PSR.goto(0, -300)


def retry():
    global collide
    global lose
    collide = False
    lose = False
    return lose
def check_collide(tur1, tur2):
    global collide
    if ((tur1.xcor() < (tur2.xcor() + 23)) and (tur1.xcor() > (tur2.xcor() - 23)) and (tur1.ycor() < (tur2.ycor() + 23)) and (tur1.ycor() > (tur2.ycor() - 23))):
        collide = True
    return collide
toa_do_goc = 0
mkmkmk = 0
def rand_spot(ob):
    global score
    if ob.ycor() < -430:
        ob.setx(random.uniform(-200, 200))
        ob.sety(430)
        ob.dy = random.uniform(4.0, 3.0)
        score += 1
        score_points.clear()
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")
def first_ran_spot(ob):
    ob.setx(random.uniform(-200, 200))
    ob.sety(430)
    ob.dy = random.uniform(0.5, 0.7)
def back_up_time():
    obs.backward(random.randint(20,50))
    obs1.backward(random.randint(20,50))
    obs2.backward(random.randint(20,50))
    obs3.backward(random.randint(20,50))
    obs4.backward(random.randint(20,50))
    obs5.backward(random.randint(20,50))
def stop_game () :
    time.sleep(random.randint(3,9))
def move_up():
    if tur.ycor() < 320:
        tur.goto(tur.xcor(), tur.ycor() + 20)

def move_down():
    if tur.ycor() > -320:
        tur.goto(tur.xcor(), tur.ycor() - 20)

def move_right():
    if tur.xcor() < 190:
        tur.goto(tur.xcor() + 20, tur.ycor())

def move_left():
    if tur.xcor() > -190:
        tur.goto(tur.xcor() - 20, tur.ycor())
def color () :
    tur.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
def die () :
    game = False
s.onkey(retry, "space")
s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.onkeypress(stop_game,"p")
s.onkeypress(color,"m")
s.onkeypress(back_up_time,"l")
s.onkeypress(die,"z")

s.listen()

while game:
    if lose == False:
        GO.clear()
        PSR.clear()

        obs.showturtle()
        obs1.showturtle()
        obs2.showturtle()
        obs3.showturtle()
        obs4.showturtle()
        obs5.showturtle()
        tur.showturtle()

        score = 0


        score_points.clear()
        high_score_points.clear()

        first_ran_spot(obs)
        first_ran_spot(obs1)
        first_ran_spot(obs2)
        first_ran_spot(obs3)
        first_ran_spot(obs4)
        first_ran_spot(obs5)


        score_points.goto(-190, 320)
        high_score_points.goto(-190, 290)
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")
        high_score_points.write("HIGHSCORE: " + str(high_score), font = ('', 15), align = "left")
        S5GO()
        tur.goto(0, -320)
        while lose == False:
            s.update()

            obs.sety(obs.ycor() - obs.dy)
            obs1.sety(obs1.ycor() - obs1.dy)
            obs2.sety(obs2.ycor() - obs2.dy)
            obs3.sety(obs3.ycor() - obs3.dy)
            obs4.sety(obs4.ycor() - obs4.dy)
            obs5.sety(obs5.ycor() - obs5.dy)
            obs.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs1.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs2.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs3.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs4.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs5.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            s.bgcolor((random.randint(0,90),random.randint(0,90),random.randint(0,90)))
            rand_spot(obs)      # random spot
            rand_spot(obs1)
            rand_spot(obs2)
            rand_spot(obs3)
            rand_spot(obs4)
            rand_spot(obs5)
            check_collide(tur, obs)
            check_collide(tur, obs1)
            check_collide(tur, obs2)
            check_collide(tur, obs3)
            if collide == True:
                lose = True

    if lose == True:
        tur.hideturtle()
        obs.hideturtle()
        obs1.hideturtle()
        obs2.hideturtle()
        obs3.hideturtle()
        obs4.hideturtle()
        obs5.hideturtle()

        score_points.clear()
        high_score_points.clear()

        if high_score < score:
            high_score = score

        score_points.goto(0, -100)
        high_score_points.goto(0, -200)
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "center")
        high_score_points.write("HIGHSCORE: " + str(high_score), font = ('', 15), align = "center")
        GO.write("GAME OVER", font = ('', 30), align = "center")
        PSR.write("Press space to try again", font = ('', 20), align = "center")

        while lose == True:
            s.update()
            #tur.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            #s.bgcolor((random.randint(0,90),random.randint(0,90),random.randint(0,90)))
            obs.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs1.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs2.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs3.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs4.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            obs5.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
