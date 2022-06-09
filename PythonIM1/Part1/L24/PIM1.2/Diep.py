# Write your code here :-)
import turtle
import random
import time

game = True
lose = False
collide = False
score = 0
high_score = 0

s = turtle.Screen()
s.setup(450, 900)
s.bgcolor("darkgrey")
s.title("Turtle Racing 2")
s.tracer(0)

tur = turtle.Turtle()
tur.shape("turtle")
tur.shapesize(1.5)
tur.penup()
tur.fillcolor("violet")
tur.pencolor("purple")
tur.left(90)
tur.goto(0,-430)
tur.ondrag(tur.goto)

tle = turtle.Turtle()
tle.shape("turtle")
tle.shapesize(1.5)
tle.penup()
tle.fillcolor("cyan")
tle.pencolor("blue")
tle.left(90)
tle.goto(0,-430)
tle.ondrag(tle.goto)

# obs is the obstacle
obs = turtle.Turtle()
obs.shape('triangle')
obs.shapesize(1)
obs.setheading(90)
obs.penup()
obs.pencolor("pink")
obs.fillcolor("red")

obs1 = obs.clone()
obs2 = obs.clone()
obs3 = obs.clone()
obs4 = obs.clone()
obs5 = obs.clone()
obs6 = obs.clone()
obs7 = obs.clone()
obs8 = obs.clone()
obs9 = obs.clone()
obs10 = obs.clone()

background_colors = ["red", "blue", "green", "orange", "purple", "gold", "azure","beige", "yellow"]
randomBackground = random.choice(background_colors)

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

GO = turtle.Turtle()
GO.penup()
GO.pencolor("white")
GO.fillcolor("white")
GO.hideturtle()
GO.goto(0, 100)

PSR = turtle.Turtle()
PSR.penup()
PSR.pencolor("white")
PSR.fillcolor("white")
PSR.hideturtle()
PSR.goto(0, -300)

def retry():
    global collide
    global lose
    collide = False
    lose = False
    return lose
    s.bgcolor(random)

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

def W():
    if tle.ycor() < 430:
        tle.goto(tle.xcor(), tle.ycor() + 20)

def S():
    if tle.ycor() > -430:
        tle.goto(tle.xcor(), tle.ycor() - 20)

def D():
    if tle.xcor() < 190:
        tle.goto(tle.xcor() + 20, tle.ycor())

def A():
    if tle.xcor() > -190:
        tle.goto(tle.xcor() - 20, tle.ycor())

s.onkey(retry, "space")
s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_right, "Right")
s.onkeypress(move_left, "Left")
s.onkeypress(W, "w")
s.onkeypress(S, "s")
s.onkeypress(D, "d")
s.onkeypress(A, "a")
s.listen()

def check_collide_tur(tur1, tur2):
    global collide
    if ((tur1.xcor() < (tur2.xcor() + 23)) and (tur1.xcor() > (tur2.xcor() - 23)) and (tur1.ycor() < (tur2.ycor() + 23)) and (tur1.ycor() > (tur2.ycor() - 23))):
        collide = True
    return collide

def check_collide_tle(tle1, tle2):
    global collide
    if ((tle1.xcor() < (tle2.xcor() + 23)) and (tle1.xcor() > (tle2.xcor() - 23)) and (tle1.ycor() < (tle2.ycor() + 23)) and (tle1.ycor() > (tle2.ycor() - 23))):
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

while game:
    randomBackground = random.choice(background_colors)
    s.bgcolor(randomBackground)
    if lose == False:
        GO.clear()
        PSR.clear()

        obs.showturtle()
        obs1.showturtle()
        obs2.showturtle()
        obs3.showturtle()
        obs4.showturtle()
        obs5.showturtle()
        obs6.showturtle()
        obs7.showturtle()
        obs8.showturtle()
        obs9.showturtle()
        obs10.showturtle()
        tur.showturtle()
        tle.showturtle()

        score = 0

        score_points.clear()
        high_score_points.clear()

        first_ran_spot(obs)
        first_ran_spot(obs1)
        first_ran_spot(obs2)
        first_ran_spot(obs3)
        first_ran_spot(obs4)
        first_ran_spot(obs5)
        first_ran_spot(obs6)
        first_ran_spot(obs7)
        first_ran_spot(obs8)
        first_ran_spot(obs9)
        first_ran_spot(obs10)

        score_points.goto(-220, 425)
        high_score_points.goto(-220, 400)
        score_points.write("SCORE: " + str(score), font = ('', 15), align = "left")
        high_score_points.write("HIGHSCORE: " + str(high_score), font = ('', 15), align = "left")

        S5GO()
        tur.goto(0, -430)        #after the countdown, the turtle should be back at the original location
        tle.goto(0, -430)
        while lose == False:
            s.update()

            obs.sety(obs.ycor() - obs.dy)
            obs1.sety(obs1.ycor() - obs1.dy)
            obs2.sety(obs2.ycor() - obs2.dy)
            obs3.sety(obs3.ycor() - obs3.dy)
            obs4.sety(obs4.ycor() - obs4.dy)
            obs5.sety(obs5.ycor() - obs5.dy)
            obs6.sety(obs6.ycor() - obs6.dy)
            obs7.sety(obs7.ycor() - obs7.dy)
            obs8.sety(obs8.ycor() - obs8.dy)
            obs9.sety(obs9.ycor() - obs9.dy)
            obs10.sety(obs10.ycor() - obs10.dy)

            rand_spot(obs)
            rand_spot(obs1)
            rand_spot(obs2)
            rand_spot(obs3)
            rand_spot(obs4)
            rand_spot(obs5)
            rand_spot(obs6)
            rand_spot(obs7)
            rand_spot(obs8)
            rand_spot(obs9)
            rand_spot(obs10)

            check_collide_tur(tur, obs)
            check_collide_tur(tur, obs1)
            check_collide_tur(tur, obs2)
            check_collide_tur(tur, obs3)
            check_collide_tur(tur, obs4)
            check_collide_tur(tur, obs5)
            check_collide_tur(tur, obs6)
            check_collide_tur(tur, obs7)
            check_collide_tur(tur, obs8)
            check_collide_tur(tur, obs9)
            check_collide_tur(tur, obs10)

            check_collide_tle(tle, obs)
            check_collide_tle(tle, obs1)
            check_collide_tle(tle, obs2)
            check_collide_tle(tle, obs3)
            check_collide_tle(tle, obs4)
            check_collide_tle(tle, obs5)
            check_collide_tle(tle, obs6)
            check_collide_tle(tle, obs7)
            check_collide_tle(tle, obs8)
            check_collide_tle(tle, obs9)
            check_collide_tle(tle, obs10)

            if collide == True:
                lose = True

    if lose == True:
        tur.hideturtle()
        tle.hideturtle()
        obs.hideturtle()
        obs1.hideturtle()
        obs2.hideturtle()
        obs3.hideturtle()
        obs4.hideturtle()
        obs5.hideturtle()
        obs6.hideturtle()
        obs7.hideturtle()
        obs8.hideturtle()
        obs9.hideturtle()
        obs10.hideturtle()

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


