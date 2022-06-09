import turtle
tina = turtle.Turtle()
tina.shape('turtle')

colors_list = ['red','orange','yellow','green','blue','purple','white']
size = 200
y = 0
for color in colors_list:
    tina.goto(0,y)
    tina.pendown()
    tina.begin_fill()
    tina.color(color)
    tina.circle(size)
    tina.end_fill()
    y = y + 20
    size = size - 20
    tina.penup()
