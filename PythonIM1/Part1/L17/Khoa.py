import turtle
from turtle import Screen
import random

tree = turtle.Turtle()
pine_tree = turtle.Turtle()
tree.hideturtle()
pine_tree.hideturtle()
speed
def Onclick(x,y):
    random1 = random.randint(0,1)
    if random1 == 1:
        #Ve cay tron
        tree.penup()
        tree.goto(x,y)
        tree.pendown()

        tree.color('green')
        tree.begin_fill()

        tree.circle(10)
        tree.end_fill()
        tree.backward(5)
        tree.begin_fill()
        tree.color('brown')
        for x in range(2):
            tree.forward(10)
            tree.right(90)
            tree.forward(20)
            tree.right(90)
        tree.end_fill()
    else:
        #Ve cay tam giac
        pine_tree.penup()
        pine_tree.goto(x,y)
        pine_tree.pendown()

        pine_tree.color('green')
        pine_tree.begin_fill()
        for x in range(3):

            pine_tree.forward(30)
            pine_tree.left(120)
        pine_tree.end_fill()
        pine_tree.forward(10)
        pine_tree.begin_fill()
        pine_tree.color('brown')
        for x in range(2):
            pine_tree.forward(10)
            pine_tree.right(90)
            pine_tree.forward(20)
            pine_tree.right(90)
        pine_tree.end_fill()


s = Screen()
s.onscreenclick(Onclick, 1)
s.listen()
s.bgcolor('blue')