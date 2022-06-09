import turtle

Player1 = turtle.Turtle()
Player1.penup()
Player1.color('red')
Player1.shape('turtle')
Player1.goto(0,0)
Player1.pendown()

Player2 = turtle.Turtle()
Player2.penup()
Player2.color('blue')
Player2.shape('turtle')
Player2.goto(0,100)
Player2.pendown()

Player1.setx(100)
Player2.setx(100)
