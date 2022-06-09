import turtle
tina = turtle.Turtle()
tina.shape('turtle')

vi_tri = [0,40,80,120]

for x in vi_tri:
    tina.goto(x,0)
    tina.pendown()
    tina.circle(30)
    tina.penup()
