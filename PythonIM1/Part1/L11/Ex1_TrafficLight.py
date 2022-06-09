import turtle
import time

#Tạo khung đèn giao thông
turtle.color('black')
turtle.begin_fill()
turtle.forward(50)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

#Tạo 3 nhân vật bóng đèn
yellow_light = turtle.Turtle()
yellow_light.shape('circle')
yellow_light.color('yellow')

red_light = turtle.Turtle()
red_light.shape('circle')
red_light.color('red')

green_light = turtle.Turtle()
green_light.shape('circle')
green_light.color('green')

yellow_light.begin_fill()
yellow_light.penup()
yellow_light.forward(25)
yellow_light.left(90)
yellow_light.forward(50)
yellow_light.color('gray')

red_light.begin_fill()
red_light.penup()
red_light.forward(25)
red_light.left(90)
red_light.forward(100)
red_light.color('gray')

green_light.begin_fill()
green_light.penup()
green_light.forward(25)
green_light.left(90)
green_light.forward(150)
green_light.color('gray')

while True:
    green_light.color('green')
    red_light.color('gray')
    yellow_light.color('gray')
    time.sleep(5)

    green_light.color('gray')
    red_light.color('gray')
    yellow_light.color('yellow')
    time.sleep(1)

    green_light.color('gray')
    red_light.color('red')
    yellow_light.color('gray')
    time.sleep(5)
