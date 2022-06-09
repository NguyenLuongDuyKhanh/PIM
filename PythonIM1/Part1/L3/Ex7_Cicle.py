import turtle
tina = turtle.Turtle()
tina.shape('turtle')

vitri_list = [20,40,60]

y = 0
size = 150
tina.penup()

for vitri in vitri_list:
    tina.goto(0,y + vitri)
    tina.pendown()
    #tina.begin_fill()
    tina.circle(size)
    #tina.end_fill()
    y = y + 20
    size = size - 40
    tina.penup()
