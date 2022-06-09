import turtle
tina = turtle.Turtle()
tina.shape('turtle')

from turtle import Screen
screen = Screen()
screen.colormode(255)

#Lớp màu đỏ
tina.penup()
tina.goto(0,0)
tina.pendown()
tina.begin_fill()
tina.color((255,0,0))
tina.circle(200)
tina.end_fill()

#Lớp màu cam
tina.penup()
tina.goto(0,0)
tina.pendown()
tina.begin_fill()
tina.color((254,183,9))
tina.circle(150)
tina.end_fill()
