# Write your code here :-)
import time
import turtle

# setting up screen
s = turtle.Screen()
s.setup(450, 900)
s.bgcolor("black")
s.title("turtle racing 2")



s.tracer(1)


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
obs1.goto(100,100)
obs2 = obs.clone()
obs2.goto(100,200)
obs3 = obs.clone()
obs3.goto(100,300)

# creating turtle and function to count down
CD = turtle.Turtle()
CD.penup()
CD.hideturtle()
CD.pencolor("white")
CD.fillcolor("white")
CD.goto(0, 100)

def S5GO():
    for i in range(5):
        CD.write(str(i), move = False, font = ('', 72), align = "center")
        time.sleep(1)
        CD.clear()
    CD.write("GO!", font=('', 72), align='center')
    time.sleep(.5)
    CD.clear()

S5GO()
obs.showturtle()
obs1.showturtle()
obs2.showturtle()
obs3.showturtle()
tur.showturtle()