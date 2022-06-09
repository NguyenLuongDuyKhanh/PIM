# Write your code here :-)
import turtle

tina = turtle.Turtle()
tina.speed(1)
# Cot = [0,50,100,150,200,250,300,350]
# Hang = [0,50,100,150,200,250,300,350]
Cot = [0, 50]
Hang = [0, 50]
for HangNgang in Hang:
    for HangDoc in Cot:
        # if ((HangNgang+HangDoc) % 2) == 0:
        #    tina.begin_fill()
        tina.goto(HangNgang, HangDoc + 50)
        tina.goto(HangNgang + 50, HangDoc + 50)
        tina.goto(HangNgang + 50, HangDoc)
        tina.goto(HangNgang, HangDoc)
        tina.goto(HangNgang + 50, HangDoc)
        # if ((HangNgang+HangDoc) % 2) == 0:
        #    tina.end_fill()
        # tina.forward(50)

    # tina.backward(400)
    # tina.left(90)
    # tina.forward(50)
    # tina.right(90)
