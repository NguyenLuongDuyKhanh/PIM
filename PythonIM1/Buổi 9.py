import turtle
import time
import random

turtle1 = turtle.Turtle()
turtle1.color("red")
turtle1.penup()
turtle1.shape('turtle')
turtle1.left(90)
turtle1.goto(-200,-200)

turtle2 = turtle.Turtle()
turtle2.color("orange")
turtle2.penup()
turtle2.shape('turtle')
turtle2.left(90)
turtle2.goto(-100,-200)

turtle3 = turtle.Turtle()
turtle3.color("yellow")
turtle3.penup()
turtle3.shape('turtle')
turtle3.left(90)
turtle3.goto(0,-200)

turtle4 = turtle.Turtle()
turtle4.color("green")
turtle4.penup()
turtle4.shape('turtle')
turtle4.left(90)
turtle4.goto(100,-200)

turtle5 = turtle.Turtle()
turtle5.color("indigo")
turtle5.penup()
turtle5.shape('turtle')
turtle5.left(90)
turtle5.goto(200,-200)

arbitration = turtle.Turtle()
arbitration.write(3, font=('', 72), align='center')
time.sleep(1)
arbitration.clear()
arbitration.write(2, font=('', 72), align='center')
time.sleep(1)
arbitration.clear()
arbitration.write(1, font=('', 72), align='center')
time.sleep(1)
arbitration.clear()
arbitration.write('GO!', font=('', 72), align='center')
time.sleep(1)
arbitration.clear()

arbitration.hideturtle()

for i in range(100):
    turtle1.forward(random.randint(1,10))
    turtle2.forward(random.randint(1,10))
    turtle3.forward(random.randint(1,10))
    turtle4.forward(random.randint(1,10))
    turtle5.forward(random.randint(1,10))

# check which turtle wins
score = [turtle1.ycor(), turtle2.ycor(), turtle3.ycor(), turtle4.ycor(), turtle5.ycor()]
color = ["RED", "ORANGE", "YELLOW", "GREEN", "INDIGO"]
win = 0
for i in range(4):
    if score[win] > score[i+1]:
        win = win
    else:
        win = i + 1
win_statement = (color[win] + " TURTLE WINS!!!")
arbitration.write(win_statement, font = ('', 52), align = "center")