import turtle
from turtle import Screen

tina = turtle.Turtle()
tina.hideturtle()
screen = Screen()

def drawtree(x,y):
    tina.penup()
    tina.goto(x,y)
    tina.pendown()
    tina.color('green')
    tina.begin_fill()
    tina.circle(10)
    tina.end_fill()
    tina.backward(5)
    tina.color('brown')
    tina.begin_fill()
    for x in range(4):
        tina.fd(10)
        tina.rt(90)
    tina.end_fill()

def draw(x,y):
    tina.penup()
    tina.goto(x,y)
    tina.pendown()
    tina.color('green')
    tina.begin_fill()
    tina.backward(10)
    tina.forward(10)
    tina.left(120)
    tina.forward(20)
    tina.left(120)
    tina.forward(20)
    tina.left(120)
    tina.forward(10)
    tina.color('brown')
    tina.begin_fill()
    for x in range(4):
        tina.fd(10)
        tina.rt(90)
    tina.end_fill()
screen.onscreenclick(draw,1)
screen.listen()
