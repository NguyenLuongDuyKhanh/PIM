import turtle
import random

tina = turtle.Turtle()
tina.penup()

while True:
    tina.color(random.choice(['red','green','blue','yellow','orange','black','pink']))
    tina.begin_fill()
    tina.goto(random.randint(-100,100),random.randint(-100,100))
    tina.circle(random.randint(0,50))
    tina.end_fill()
