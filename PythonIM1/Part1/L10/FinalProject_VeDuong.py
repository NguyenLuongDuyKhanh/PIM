import turtle
import random

charlie = turtle.Turtle()
charlie.speed(0)
charlie.penup()
charlie.goto(-140, 140)

for step in range(15):
  charlie.write(step, align='center')
  charlie.right(90)

  for num in range(8):
    charlie.penup()
    charlie.forward(10)
    charlie.pendown()
    charlie.forward(10)

  charlie.penup()
  charlie.backward(160)
  charlie.left(90)
  charlie.forward(20)
turtle.done()