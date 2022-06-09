import turtle as t

# SETTING UP THE SCREEN
s = t.Screen()
s.setup(900, 900)
s.setworldcoordinates(-450, -450, 450, 450)
s.bgcolor("black")
s.title("Game of Jungle")

# CREATING THE TURTLE WITH DIFFERENT FUNCTIONS
# CREATING A TURTLE FOR WRITING TEXT
t_text = t.Turtle()
t_text.pencolor("cyan")
t_text.hideturtle()
t_text.penup()
t_text.speed(0)
# CREATING A TURTLE FOR DRAWING BOXES OF CHOICES
t_box = t_text.clone()
t_box.pencolor("cyan")
t_box.pensize(3)
# CREATING A TURTLE FOR CHOOSING LEFT (L) OR RIGHT(R)
t_choice = t_text.clone()
t_choice.shape("circle")
t_choice.speed(3)
s.onscreenclick(t_choice.goto)

# CREATING A TURTLE FOR WRITING LEFT/RIGHT IN THE BOXES
t_LR = t_text.clone()
t_LR.pencolor("cyan")
t_LR.pensize(3)

# DRAWING THE CHOOSING BOXES
t_box.penup()
t_box.goto(-450, -150)
t_box.pendown()
t_box.goto(450, -150)
t_box.penup()
t_box.goto(0, -150)
t_box.pendown()
t_box.goto(0, -450)

# WRITING LEFT/RIGHT IN THE BOXES
t_LR.goto(-225, -300)
t_LR.write("TRÁI", font=('', 40), align="center")
t_LR.goto(225, -300)
t_LR.write("PHẢI", font=('', 40), align="center")

s.mainloop()