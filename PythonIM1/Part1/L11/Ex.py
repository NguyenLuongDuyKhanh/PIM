import time
import random
import turtle
tina = turtle.Turtle()
tina.shape('classic')
tina.shapesize(0.01)

tina.penup()
tina.goto(0, 0)
tina.pendown()

vuong = 'square'
tron = 'circle'

print('Choose one of these shapes')
time.sleep(1)
print("square")
time.sleep(1)
print("circle")

time.sleep(1)
choose_shape = (input('The shape you choose: '))

# Square
so_canh_hinh_vuong = 4
goc_hinh_vuong = 180 - 90

if choose_shape == vuong:
    for x in range(so_canh_hinh_vuong):

        tina.forward(Canh)
        tina.left(goc_hinh_vuong)
else:
    Ban_kinh = int(input('Nhập bán kính: '))
    tina.circle(Ban_kinh)
