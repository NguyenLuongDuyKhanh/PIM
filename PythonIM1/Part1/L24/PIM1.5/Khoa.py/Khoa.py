import random
import turtle
import time
from turtle import Screen
tina = turtle.Turtle()

def nhan_vat():
    tina.left(90)
    tina.color("blue")
    tina.penup()
score = 0
def Thoi_Gian():
    timer = 6
    for x in range(6):
        timer = timer - 1

        time.sleep(1)
        e.clear()
    e.write("Go", font=("", 72), align="center")
    time.sleep(1)
    e.clear()
def Thuc_Hien_Khi_Nhan_A():
    tina.setx(tina.xcor() - 5)


############################################################
def Thuc_Hien_Khi_Nhan_W():
    tina.sety(tina.ycor() + 5)


############################################################
def Thuc_Hien_Khi_Nhan_S():
    tina.sety(tina.ycor() - 5)


###########################################################


def Thuc_Hien_Khi_Nhan_D():
    tina.setx(tina.xcor() + 5)
    if tina.xcor()>100:
        tina.color('yellow')
################################################################
def replay():
    global gamecore
    gamecore = True
    score = 0
    e.clear()
    Spacetoreplay.clear()
    displayscore.clear()


################################################################
Spacetoreplay = turtle.Turtle()
Spacetoreplay.hideturtle()
Spacetoreplay.penup()
Spacetoreplay.color('red')
################################################################

s = turtle.Screen()
s.setup(800,1000)
s.title("turtle racin")
s.bgcolor("black")
s.tracer(0)
################################################################
s.onkeypress(Thuc_Hien_Khi_Nhan_A, "a")


###################################################################
s.onkeypress(Thuc_Hien_Khi_Nhan_W, "w")


#################################################################

s.onkeypress(Thuc_Hien_Khi_Nhan_S, "s")


#################################################################
s.onkeypress(Thuc_Hien_Khi_Nhan_D, "d")


#################################################################

#################################################################
tina.ondrag(tina.goto)
#########################################

################################################################
s.onkeypress(Thuc_Hien_Khi_Nhan_A, "Left")


###################################################################
s.onkeypress(Thuc_Hien_Khi_Nhan_W, "Up")


#################################################################

s.onkeypress(Thuc_Hien_Khi_Nhan_S, "Down")

#######################################################
############################################################
s.onkeypress(replay, "space")



#################################################################
s.onkeypress(Thuc_Hien_Khi_Nhan_D, "Right")
s.listen()
#################################################################
food = turtle.Turtle()
food.shape('circle')
food.color('green')
food.penup()
food.goto(random.randint(-400, 400), 500)
food.right(90)

####################################################
displayscore = turtle.Turtle()
displayscore.color("red")
displayscore.penup()
displayscore.goto(-380,-480)
displayscore.pendown()
displayscore.write(score)
displayscore.hideturtle()
################
blocc = turtle.Turtle()
blocc.shape("circle")
blocc.color(random.choice(["blue", "yellow", "pink"]))
blocc.penup()
###################
blocc2 = turtle.Turtle()
blocc2 = blocc.clone()
blocc2.shape("triangle")
blocc2.goto(0, 50)
blocc2.penup()
############################
blocc3 = turtle.Turtle()
blocc3.shape("square")
blocc3.color(random.choice(["blue", "yellow", "pink"]))
blocc3.penup()

###########################
blocc4 = turtle.Turtle()
blocc4.shape("classic")
blocc4.color(random.choice(["blue", "yellow", "pink"]))
blocc4.penup()

##########################

blocc.shapesize(random.randint(1, 3))
blocc2.shapesize(random.randint(1, 3))
blocc3.shapesize(random.randint(1, 3))
blocc4.shapesize(random.randint(1, 3))
food.shapesize(random.randint(1, 3))

#########################################
blocc.goto(random.randint(-400, 400), 500)
blocc2.goto(random.randint(-400, 400), 500)
blocc3.goto(random.randint(-400, 400), 500)
blocc4.goto(random.randint(-400, 400), 500)

###############################################
e = turtle.Turtle()
e.hideturtle()
e.penup()
e.color("red")
e.goto(0, 300)
##############################################
#Thoi_Gian()
tina.hideturtle()
nhan_vat()
tina.showturtle()
##############################################
blocc.right(90)
blocc2.right(90)
blocc3.right(90)
blocc4.right(90)

gamecore = True

def kiemtravacham(tina , blocc):
    if (tina.xcor() > blocc.xcor() - 20) and (tina.xcor() < blocc.xcor()+20) and (tina.ycor() > blocc.ycor()-20)  and (tina.ycor() < blocc.ycor()+20):
        global gamecore
        print("co va cham")
        gamecore = False

def rand_spot(blocc):
    global score
    if blocc.ycor() < -500:
        blocc.hideturtle()
        blocc.goto(random.randint(-400,400),500)
        blocc.showturtle()
        score = score + 1
        print(score)
        displayscore.clear()
        displayscore.write(score,font=("", 72))

def first_ran_spot(ob):
    ob.setx(random.uniform(-200, 200))
    ob.sety(430)
    ob.dy = random.uniform(0.5, 0.7)

def eating(tina , food):
    if (tina.xcor() > food.xcor() - 20) and (tina.xcor() < food.xcor()+20) and (tina.ycor() > food.ycor()-20)  and (tina.ycor() < food.ycor()+20):
        global score
        tina.color(random.choice(['red','blue','green','white','pink','yellow','purple']))

        score = score + 10
        food.goto(1000,1000)
        food.hideturtle()
        displayscore.clear()
        displayscore.write(score,font=("", 72))
        food.showturtle()
        food.goto(random.randint(-400, 400), 500)


while True:
    if gamecore == True:
        blocc.showturtle()
        blocc2.showturtle()
        blocc3.showturtle()
        blocc4.showturtle()
        food.showturtle()
        tina.showturtle()
        score = 0
        displayscore.clear()
        Spacetoreplay.clear()
        displayscore.goto(-380,-480)
        displayscore.write(score,font=("", 72))

        first_ran_spot(blocc)
        first_ran_spot(blocc2)
        first_ran_spot(blocc3)
        first_ran_spot(blocc4)
        tina.goto(0,-400)
        while gamecore == True:
            s.update()

            blocc.forward(1)
            blocc2.forward(1)
            blocc3.forward(1)
            blocc4.forward(1)
            food.forward(1)

            rand_spot(blocc)
            rand_spot(blocc2)
            rand_spot(blocc3)
            rand_spot(blocc4)
            rand_spot(food)

            kiemtravacham(tina,blocc)
            kiemtravacham(tina,blocc4)
            kiemtravacham(tina,blocc2)
            kiemtravacham(tina,blocc3)
            eating(tina,food)

    if gamecore == False:
        displayscore.penup()
        blocc.hideturtle()
        blocc2.hideturtle()
        blocc3.hideturtle()
        blocc4.hideturtle()
        tina.hideturtle()
        displayscore.clear()
        displayscore.goto(0,300)
        displayscore.write(score, font=("", 72), align="center")
        Spacetoreplay.goto(0,250)
        Spacetoreplay.write("Press space to replay lul", font=("",52), align="center")
        while gamecore == False:
            s.update()