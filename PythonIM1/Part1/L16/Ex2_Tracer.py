import turtle
from turtle import Screen
import random
import time
tina = turtle.Turtle()
s = Screen()
s.tracer(0)

for x in range(10):
    s.update()
    tina.penup()
    tina.goto(random.randint(0,200),random.randint(0,200))
    tina.pendown()
    tina.circle(50)
    time.sleep(1)
