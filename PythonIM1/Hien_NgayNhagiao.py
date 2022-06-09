import turtle
import time
import random

s = turtle.Screen()
s.setup(400, 400)
s.bgcolor("black")

color_num = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

s1 = turtle.Turtle()
s1.shapesize(0.01)
s1.color("white")
s1.penup()

s1.goto(0, -100)
for i in range(5):
    s1.write(str(abs(5-i)), font = ('', 72), align = "center")
    time.sleep(1)
    s1.clear()
s1.write("GO!", font=('', 72), align='center')
time.sleep(1)
s1.clear()
for x in range(5):
    s1.write("20/11", font = ('', 100), align = "center")
    s1.color(random.choice(color_num))
time.sleep(0.5)
s1.clear()
for y in range(5):
    s1.write("Chúc mừng ngày 20/11", font = ('', 50), align = "center")
    s1.color(random.choice(color_num))
time.sleep(1)
s1.clear()
for z in range(5):
    s1.write("Em chúc thầy luôn vui vẻ, mạnh khỏe", font = ('', 50), align = "center")
    s1.color(random.choice(color_num))
time.sleep(1)
s1.clear()
while True:
    s1.write("Cảm ơn thầy vì đã dạy chúng em từ mùa hè đến nay!", font = ('', 40), align = "center")
    s1.color(random.choice(color_num))