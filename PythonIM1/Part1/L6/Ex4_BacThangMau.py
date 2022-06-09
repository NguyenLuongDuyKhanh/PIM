# Write your code here :-)
import turtle

#Set screenmode
from turtle import Screen
screen = Screen()
screen.colormode(255)

tina = turtle.Turtle()
green = 255
blue = 255
for bacthang in range(50):
    green = green - 10
    blue = blue - 10
    tina.color((0, green, blue))
    tina.forward(10)
    tina.left(90)
    tina.forward(10)
    tina.right(90)
