# Write your code here 😃
from turtle import *
from turtle import Screen
screen = Screen()
Green = 245
Blue = 247
screen.colormode(255)
import turtle
tina = turtle.Turtle()
tina.shape('turtle')
import turtle
tima = turtle.Turtle()
tima.shape('turtle')
for x in range(1,100):
    Green = Green - 10
    Blue = Blue - 10
    tina.color((0, Green, Blue))
    tima.color((0, Green, Blue))
    tina.forward(12)
    tima.forward(12)
    tina.left(90)
    tima.right(90)
    tina.forward(12)
    tima.forward(12)
    tina.right(90)
    tima.left(90)
