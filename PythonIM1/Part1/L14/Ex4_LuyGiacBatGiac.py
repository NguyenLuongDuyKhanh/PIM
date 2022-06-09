import turtle
tur = turtle.Turtle()

tur.penup()
tur.goto(103, 21)
tur.pendown()
for i in range(6):
    tur.forward(20)
    tur.left(360/6)

tur.penup()
tur.goto(-40, -80)
tur.pendown()
for i in range(8):
    tur.forward(20)
    tur.left(360/8)