import turtle
import random

s = turtle.Screen()
s.setup(1000, 1000)

bob = turtle.Turtle()
bob.shape("turtle")
bob.pencolor("black")
bob.pensize(2)
bob.speed(-1)
turtle.colormode(255)

a = 360 / 90

for i in range(10):
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    red1 = random.randrange(0, 255)
    green1 = random.randrange(0, 255)
    blue1 = random.randrange(0, 255)
    size = random.uniform(3, 6)
    x_loc = random.randrange(-400, 400)
    y_loc = random.randrange(-300, 500)
    bob.penup()
    bob.goto(x_loc, y_loc)
    bob.pendown()
    col = (red, green, blue)
    col1 = (red1, green1, blue1)
    bob.fillcolor(col)
    bob.pencolor(col1)
    bob.begin_fill()
    for i in range(90):
        bob.forward(size)
        bob.right(a)
    bob.end_fill()
