import turtle
import time

lose = False
score = 0
game = True

# setting up screen
screen = turtle.Screen()
screen.title('Pong')
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.tracer(0)

# making a turtle into a ball
ball = turtle.Turtle()
ball.penup()
ball.fillcolor("red")
ball.pencolor("red")
ball.shape("circle")
ball.shapesize(2,2)
ball.dx = .100                            # ball's x-cor speed
ball.dy = .100                            # ball's y-cor speed

# making a paddle
paddle = turtle.Turtle()
paddle.penup()
paddle.fillcolor("black")
paddle.pencolor("blue")
paddle.shape("square")
paddle.shapesize(1, 5)
paddle.goto(0, -250)
paddle.ondrag(paddle.goto)



def move_left():
    if paddle.xcor() > -330:
        paddle.goto(paddle.xcor() - 20, paddle.ycor())

def move_right():
    if paddle.xcor() < 325:
        paddle.goto(paddle.xcor() + 20, paddle.ycor())

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.listen()

# keep on updating the screen while it's not game over
while game == True:
    if lose == False:
        while lose == False:
            screen.update()

            # Moving Ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Border checking
            if ball.ycor() > 290 or ball.ycor() < -290:
                ball.dy = -ball.dy

            # Border checking
            if ball.xcor() > 390 or ball.xcor() < -390:
                ball.dx = -ball.dx

            # paddle vs ball checking
            if ((ball.ycor() < (paddle.ycor() + 10) and ball.ycor() > (paddle.ycor() -10)) and (ball.xcor() < (paddle.xcor() + 50) and ball.xcor() > (paddle.xcor() - 50))) :
                ball.dy = -ball.dy