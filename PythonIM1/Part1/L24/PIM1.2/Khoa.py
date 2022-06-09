import turtle
import random
import time

game = True
lose = False
collide = False
score = 0
high_score = 0

# setting up screen
s = turtle.Screen()
s.setup(450, 900)
s.bgcolor(0.2,0.5,0.9)
s.title("turtle racing 2")
s.tracer(0)


# tur is the main turtle to race
tur = turtle.Turtle()
tur.shape("turtle")
tur.shapesize(1.75,1.5)
tur.penup()
tur.fillcolor("blue")
tur.pencolor("blue")
tur.left(90)


tur.goto(0,-350)
tur.ondrag(tur.goto)

tur1 = turtle.Turtle()
tur1.shape("turtle")
tur1.shapesize(1.75,1.5)
tur1.penup()
tur1.fillcolor("green")
tur1.pencolor("green")
tur1.left(90)


tur1.goto(-200,-350)
tur1.ondrag(tur.goto)


# obs is the obstacle
obs = turtle.Turtle()
obs.shape("circle")
obs.shapesize(1.75, 1.75)
obs.penup()
obs.pencolor("gray")
obs.fillcolor("gray")


# cloning the first obstacle so we don't have to write this over again
obs1 = obs.clone()
obs2 = obs.clone()
obs3 = obs.clone()
obs4 = obs.clone()

#create obstacle come from the length of the screen
obs6 = turtle.Turtle()
obs6.shape('classic')
obs6.shapesize(1.75, 1.75)
obs6.penup()
obs6.pencolor("gray")
obs6.fillcolor("blue")
obs7 = obs6.clone()
obs8 = obs6.clone()

# creating score, high score turtle
score_points = turtle.Turtle()
score_points.pencolor("white")
score_points.fillcolor('white')
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

def move_up_tur1():
    if tur1.ycor() < 430:
        tur1.goto(tur1.xcor(), tur1.ycor() + 20)

def move_down_tur1():
    if tur1.ycor() > -430:
        tur1.goto(tur1.xcor(), tur1.ycor() - 20)

def move_right_tur1():
    if tur1.xcor() < 190:
        tur1.goto(tur1.xcor() + 20, tur1.ycor())

def move_left_tur1():
    if tur1.xcor() > -190:
        tur1.goto(tur1.xcor() - 20, tur1.ycor())

s.onkey(retry, "space")
s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.onkeypress(move_up_tur1, "w")
s.onkeypress(move_down_tur1, "s")
s.onkeypress(move_right_tur1, "d")
s.onkeypress(move_left_tur1, "a")
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

def rand_spot_2(ob):
    global score
    if ob.xcor() > 190:
        ob.setx(-190)
        ob.sety(random.uniform(-350, 350))
        ob.dy = random.uniform(0.5, 0.7)
        score += 1
        score_points.clear()
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")

def first_ran_spot(ob):
    ob.setx(random.uniform(-200, 200))
    ob.sety(430)
    ob.dy = random.uniform(0.5, 0.7)

def first_ran_spot_2(ob):
    ob.setx(-190)
    ob.sety(random.uniform(-350, 350))
    ob.dy = random.uniform(0.5, 0.7)

#create good present or bad present for tur.
GP = turtle.Turtle()
GP.shape("circle")
GP.shapesize(1,1)
GP.penup()
GP.fillcolor('salmon')
GP.pencolor('white')
GP.goto(500,950)

BP = turtle.Turtle()
BP.shape("circle")
BP.shapesize(1,1)
BP.penup()
BP.fillcolor('salmon')
BP.pencolor('white')
BP.goto(500,950)

def good_present(tur1,tur2):
    global score
    if ((tur1.xcor() < (tur2.xcor() + 23)) and (tur1.xcor() > (tur2.xcor() - 23)) and (tur1.ycor() < (tur2.ycor() + 23)) and (tur1.ycor() > (tur2.ycor() - 23))):
        score += 10
        GP.hideturtle()
        GP.goto(500,950)

def bad_present(tur1,tur2):
    global score
    if ((tur1.xcor() < (tur2.xcor() + 23)) and (tur1.xcor() > (tur2.xcor() - 23)) and (tur1.ycor() < (tur2.ycor() + 23)) and (tur1.ycor() > (tur2.ycor() - 23))):
        score -= 10
        BP.hideturtle()
        BP.goto(500,950)

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
        obs4.showturtle()
        obs6.showturtle()
        obs7.showturtle()
        obs8.showturtle()
        tur.showturtle()
        tur1.showturtle()
        GP.showturtle()
        BP.showturtle()
        score = 0


        score_points.clear()
        high_score_points.clear()

        first_ran_spot(obs)
        first_ran_spot(obs1)
        first_ran_spot(obs2)
        first_ran_spot(obs3)
        first_ran_spot(obs4)

        first_ran_spot_2(obs6)
        first_ran_spot_2(obs7)
        first_ran_spot_2(obs8)

        score_points.goto(-220, 350)
        high_score_points.goto(-220, 320)
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")
        high_score_points.write("HIGHSCORE: " + str(high_score), font = ('', 15), align = "left")

        S5GO()
        tur.goto(0, -360)
        tur1.goto(-200,-360)        #after the countdown, the turtle should be back at the original location
        GP.goto(random.randint(-190,190),random.randint(-350,350))
        BP.goto(random.randint(-190,190),random.randint(-350,350))
        while lose == False:
            s.update()

            obs.sety(obs.ycor() - obs.dy)
            obs1.sety(obs1.ycor() - obs1.dy)
            obs2.sety(obs2.ycor() - obs2.dy)
            obs3.sety(obs3.ycor() - obs3.dy)
            obs4.sety(obs4.ycor() - obs4.dy)

            obs6.setx(obs6.xcor() + obs6.dy)
            obs7.setx(obs7.xcor() + obs7.dy)
            obs8.setx(obs8.xcor() + obs8.dy)

            rand_spot(obs)
            rand_spot(obs1)
            rand_spot(obs2)
            rand_spot(obs3)
            rand_spot(obs4)

            rand_spot_2(obs6)
            rand_spot_2(obs7)
            rand_spot_2(obs8)

            check_collide(tur, obs)
            check_collide(tur, obs1)
            check_collide(tur, obs2)
            check_collide(tur, obs3)
            check_collide(tur, obs4)

            check_collide(tur, obs6)
            check_collide(tur, obs7)
            check_collide(tur, obs8)

            check_collide(tur1, obs)
            check_collide(tur1, obs1)
            check_collide(tur1, obs2)
            check_collide(tur1, obs3)
            check_collide(tur1, obs4)

            check_collide(tur1, obs6)
            check_collide(tur1, obs7)
            check_collide(tur1, obs8)

            good_present(tur1, GP)
            bad_present(tur1, BP)
            good_present(tur, GP)
            bad_present(tur, BP)


            if collide == True:
                lose = True

    if lose == True:
        tur.hideturtle()
        tur1.hideturtle()
        obs.hideturtle()
        obs1.hideturtle()
        obs2.hideturtle()
        obs3.hideturtle()
        obs4.hideturtle()
        obs6.hideturtle()
        obs7.hideturtle()
        obs8.hideturtle()
        GP.hideturtle()
        BP.hideturtle()


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


