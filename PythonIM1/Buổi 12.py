import turtle
import random

# create screen and turtle
cwidth = 1000               # canvas width (need more space)
clength = 1000              # canvas length
screen = turtle.Screen()    # create a screen


screen.setup(cwidth, clength, startx = None, starty = None)     # screen setting

bob = turtle.Turtle()       # create a turtle named bob
bob_1 = turtle.Turtle()
bob_2 = turtle.Turtle()
bob_3 = turtle.Turtle()

# turtle set up

#######################################################################
# change turtle pencolor() - change the outline of the turtle
# and fill(color) - changing the color inside the turtle
#
#######################################################################

# turtle line's color
bob.pencolor("black")
bob_1.pencolor("yellow")
bob_2.pencolor("red")
bob_3.pencolor("blue")

# turtle filling color
bob.fillcolor("black")       # turtle filling color when a shape is drawn and called
bob_1.fillcolor("#00fff5")
bob_2.fillcolor("#f500ff")
bob_3.fillcolor("#00fc6a")



bob.speed(-1)               # turtle's speed
bob.pensize(4)              # line's width when being drawn

# make bob to become turtle (default: arrow head)
bob.shape("turtle")
bob_1.shape("turtle")
bob_2.shape("turtle")
bob_3.shape("turtle")


# all turtle penup()
bob.penup()
bob_1.penup()
bob_2.penup()
bob_3.penup()

# bob will be drawing the starting position and goal
bob.goto(-400, 400)
bob.pendown()
bob.goto(-400, -400)
bob.penup()
bob.goto(400, -400)
bob.pendown()
bob.goto(400, 400)
bob.penup()
bob.goto(440, 350)
bob.write("Finish", True, align = "left", font = ("Arial", 15, "normal"))
bob.goto(-360, 350)
bob.write("Starting line", True, align = "left", font = ("Arial", 15, "normal"))

# OPTIONAL: bob draw a 3 lights before all run
bob.goto(-250, -535)
bob.pendown()
bob.begin_fill()
for i in range(2):
    bob.forward(500)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
bob.end_fill()
bob.penup()


# turtle starting position
# bob will be deciding who wins

bob_1.goto(-400, 300)
bob_2.goto(-400, 0)
bob_3.goto(-400, -300)

# randomize the turtle speed
bob_1.speed(2)
bob_2.speed(2)
bob_3.speed(2)

#OPTIONAL, draw 3 lights before turtles start running
bob.left(90)
bob.goto(-190, -420)
bob.pencolor("red")
bob.fillcolor("red")
bob.pendown()
bob.begin_fill()
for i in range(90):
    bob.forward(4)
    bob.right(4)
bob.end_fill()
bob.penup()
bob.goto(-50, -420)
bob.pencolor("orange")
bob.fillcolor("orange")
bob.pendown()
bob.begin_fill()
for i in range(90):
    bob.forward(4)
    bob.right(4)
bob.end_fill()
bob.penup()
bob.goto(80,-420)
bob.pencolor("green")
bob.fillcolor("green")
bob.pendown
bob.begin_fill()
for i in range(90):
    bob.forward(4)
    bob.right(4)
bob.end_fill()
bob.penup()


############################################################################################
# write if statement to see which turtle win
# because the code only from top to bottom so after the turtle run, we check
# their position if they cross the finish line or not
# then we can decide if it's draw or which turtle win and will let
# turtle bob write who win or draw on the screen
# using break to stop the for loop so it doesn't loop forever
############################################################################################

bob.hideturtle()
bob.pencolor("black")
bob.fillcolor("black")
bob.goto(0, 400)

for i in range(1000):
    bob_1.forward(random.randrange(0, 30))
    bob_2.forward(random.randrange(0, 30))
    bob_3.forward(random.randrange(0, 30))


    if (bob_1.xcor() > 400) and (bob_2.xcor() > 400) and (bob_3.xcor() >400):
        bob.write("all turtle draw", True, align = "center", font = ("Arial", 50, "normal"))
        break


    elif (bob_1.xcor() > 400) and (bob_2.xcor() > 400):
        bob.write("turtle 1 and 2 draw", True, align = "center", font = ("Arial", 50, "normal"))
        break


    elif (bob_1.xcor() > 400) and (bob_3.xcor() > 400):
        bob.write("turtle 1 and 3 draw", True, align = "center", font = ("Arial", 50, "normal"))
        break


    elif (bob_3.xcor() > 400) and (bob_2.xcor() > 400):
        bob.write("turtle 2 and 3 draw", True, align = "center", font = ("Arial", 50, "normal"))
        break


    elif (bob_1.xcor() > 400):
        bob.write("turtle 1 wins!!", True, align = "center", font = ("Arial", 50, "normal"))
        break


    elif (bob_2.xcor() > 400):
        bob.write("turtle 2 wins!!", True, align = "center", font = ("Arial", 50, "normal"))
        break


    elif (bob_3.xcor() > 400):
        bob.write("turtle 3 wins!!", True, align = "center", font = ("Arial", 50, "normal"))
        break