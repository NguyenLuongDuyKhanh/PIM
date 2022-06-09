# With obs color
# Write your code here :-)
import turtle
import random
import time

game = True
lose = False
collide = False
score = 0
high_score = 0

obsR=255
obsG=255
obsB=255
# setting up screen
s = turtle.Screen()
s.colormode(255)
s.setup(450, 900)
s.bgcolor("black")
s.title("turtle racing 2")
s.tracer(0)


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

obs1 = obs.clone()
obs2 = obs.clone()
obs3 = obs.clone()


# creating score, high score turtle
score_points = turtle.Turtle()
score_points.pencolor("white")
score_points.fillcolor("white")
score_points.penup()
score_points.hideturtle()

high_score_points = turtle.Turtle()
high_score_points.pencolor("white")
high_score_points.fillcolor("white")
high_score_points.penup()
high_score_points.hideturtle()


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


# creating turtle for gameover screen
GO = turtle.Turtle()
GO.penup()
GO.pencolor("white")
GO.fillcolor("white")
GO.hideturtle()
GO.goto(0, 100)

# making turtle for pressing space to retry the game
PSR = turtle.Turtle()
PSR.penup()
PSR.pencolor("white")
PSR.fillcolor("white")
PSR.hideturtle()
PSR.goto(0, -300)

####################################################################
# creating function to let the turtle move up, left, right, or down
# and also creating function to retry the game after losing
# remember to check edge to not let the turtle go outside
# the screen
####################################################################

def retry():
    global collide
    global lose
    collide = False
    lose = False
    return lose

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

s.onkey(retry, "space")
s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.listen()


#######################################################################################
# creating function to check collide
# creating function to give obstacle a random spot to spawn back on top
# creating function to give obstacle a random spot to first spawn when the game start
#######################################################################################


def check_collide(tur1, tur2):
    global collide
    if ((tur1.xcor() < (tur2.xcor() + 23)) and (tur1.xcor() > (tur2.xcor() - 23)) and (tur1.ycor() < (tur2.ycor() + 23)) and (tur1.ycor() > (tur2.ycor() - 23))):
        collide = True
    return collide

def rand_spot(ob):
    global score
    if ob.ycor() < -430:
        ob.setx(random.uniform(-200, 200))
        ob.sety(430)
        ob.dy = random.uniform(0.5, 0.7)
        score += 1
        score_points.clear()
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")

def first_ran_spot(ob):
    ob.setx(random.uniform(-200, 200))
    ob.sety(430)
    ob.dy = random.uniform(0.5, 0.7)

#################################################################################################################
# making a while loop to run the game forever until closing the game
# checking if lose is False or True
#################################################################################################################



while game:
    if lose == False:
        GO.clear()
        PSR.clear()

        obs.showturtle()
        obs1.showturtle()
        obs2.showturtle()
        obs3.showturtle()
        tur.showturtle()

        score = 0


        score_points.clear()
        high_score_points.clear()

        first_ran_spot(obs)
        first_ran_spot(obs1)
        first_ran_spot(obs2)
        first_ran_spot(obs3)

        score_points.goto(-220, 430)
        high_score_points.goto(-220, 400)
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")
        high_score_points.write("HIGHSCORE: " + str(high_score), font = ('', 15), align = "left")

        S5GO()
        tur.goto(0, -430)                               #after the countdown, the turtle should be back at the original location
        while lose == False:
            s.update()


            if obsR != 0:
                obsR = obsR - 1
            else:
                obsR = 255
            if obsG != 0:
                obsG = obsG - 1
            else:
                obsG = 255
            if obsB != 0:
                obsB = obsB - 1
            else:
                obsB = 255
            obs.fillcolor((obsR,255,255))
            obs1.fillcolor((255,255,obsB))
            obs2.fillcolor((255,obsG,255))
            obs3.fillcolor((obsR,obsG,obsB))

            obs.sety(obs.ycor() - obs.dy)
            obs1.sety(obs1.ycor() - obs1.dy)
            obs2.sety(obs2.ycor() - obs2.dy)
            obs3.sety(obs3.ycor() - obs3.dy)

            rand_spot(obs)
            rand_spot(obs1)
            rand_spot(obs2)
            rand_spot(obs3)

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
