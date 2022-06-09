import turtle
from turtle import Screen

s = Screen()
s.setup(500,500)
s.bgcolor('cyan')
s.title('Phan mem A')
s.tracer(0)

turtle = turtle.Turtle()
turtle.circle(100)
s.update()