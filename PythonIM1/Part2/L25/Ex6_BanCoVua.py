# Write your code here :-)
import turtle
tina = turtle.Turtle()
tina.speed(4)
for HangNgang in range(8):
    for HangDoc in range(8):
        #if ((HangNgang+HangDoc) % 2) == 0:
        #   tina.begin_fill()
        for Canh in range(4):
            tina.forward(50)
            tina.left(90)
        #if ((HangNgang+HangDoc) % 2) == 0:
        #    tina.end_fill()
        tina.forward(50)
    tina.backward(400)
    tina.left(90)
    tina.forward(50)
    tina.right(90)
