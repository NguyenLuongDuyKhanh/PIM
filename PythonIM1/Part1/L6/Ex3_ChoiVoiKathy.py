import turtle
#init tina
tina = turtle.Turtle()
tina.shape('turtle')

#init kathy
kathy = turtle.Turtle()
kathy.shape('triangle')

#Set screenmode
from turtle import Screen
screen = Screen()
screen.colormode(255)

tina.begin_fill()
tina.color((255,0,255))
tina.circle(50)
tina.end_fill()

kathy.penup()
kathy.goto(100,0)
kathy.pendown()
kathy.begin_fill()
kathy.color((0,255,255))
kathy.circle(50)
kathy.end_fill()

turtle.done()