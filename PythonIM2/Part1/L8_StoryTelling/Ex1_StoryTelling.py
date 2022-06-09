import time
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

# FUNCTION FOR CHOOSING
def choice():
    if t_choice.ycor() < -150:
        if t_choice.xcor() < 0:
            t_choice.goto(0, 0)
            return "L"
        elif t_choice.xcor() > 0:
            t_choice.goto(0, 0)
            return "R"
        else:
            t_choice.goto(0, 0)

def first_part():
    t_text.goto(0, 400)
    t_text.write(welcome_text, font=('', 25), align="center")
    t_text.goto(0, 320)
    t_text.write(game_text, font=('', 30), align="center")
    t_text.goto(0, 200)
    t_text.write("Bạn thức dậy trong một khu rừng và không biết mình đang ở đâu.", font=('', 20), align="center")
    t_text.goto(0, 150)
    t_text.write("Bạn nhìn thấy một con sông bên phải và một lâu đài bí ẩn bên trái.", font=('', 20), align="center")
    t_text.goto(0, 100)
    t_text.write("Bạn sẽ chọn đi hướng nào? T/P ?", font=('', 20),align="center")
    ans = choice()
    print(ans)
    while ans == None:
        ans = choice()
        time.sleep(1)
        t_text.goto(0, 0)
    t_text.clear()
    return ans

def left():
    t_text.goto(0, 400)
    t_text.write("Bạn đi thẳng tới lâu đài bí ẩn mà không một chút do dự.", font=('', 20),align="center")
    t_text.goto(0, 320)
    t_text.write("Trước mặt bạn là một cánh cổng lớn", font=('', 20),align="center")
    t_text.goto(0, 200)
    t_text.write("""Bạn đẩy cánh cổng mở ra và bạn nhìn thấy 2 con đường,
    trái và phải.""", font=('', 20),align="center")
    t_text.goto(0, 150)
    t_text.write("Bạn sẽ chọn đi con đường nào? T/P ?",font=('', 20),align="center")
    ans = choice()
    print(ans)
    while ans == None:
        ans = choice()
        time.sleep(1)
        t_text.goto(0, 0)
    t_text.clear()
    return ans

def right():
    t_text.write("""    Bạn đến bên bờ hồ và hớp vài ngụm nước,
    bạn cảm thấy tỉnh táo hơn.
    Đằng xa phía trên trái, bạn nhìn thấy một ngôi làng.
    Phía bên phải, bạn nhìn thấy một ông lão
    đang thu hoạch thảo mộc gần căn lều.
    Bạn sẽ chọn đi hướng nào, T/P?
    """, font=('', 20),align="center")
    ans = choice()
    print(ans)
    while ans == None:
        ans = choice()
        time.sleep(1)
        t_text.goto(0, 0)
    t_text.clear()
    return ans

def left_left():
    t_text.write("""    Bạn tìm thấy một đống vàng và trang sức.
    Chúc mừng bạn! Bạn đã trở thành người giàu có!
    KẾT THÚC
    """, font=('', 20),align="center")


def left_right():
    t_text.write("""    Bạn đi xuống một đường hầm tối đen.
    Và bạn không thể nhìn thấy bất cứ thứ gì cho đến khi
    có một đám lửa đi thẳng về phía bạn.
    Thật không may! Bạn đã bị thiêu sống.
    KẾT THÚC
    """, font=('', 20),align="center")

def right_left():
    t_text.write("""    Bạn đi thẳng tới ngôi làng.
    Bạn bắt đầu một cuộc sống bình thường mới
    như một người nông dân ở đây.
    KẾT THÚC
    """, font=('', 20),align="center")

def right_right():
    t_text.write("""    Bạn đi thẳng về phía ông lão.
    Ông ta đang lẩm bẩm một điều gì đó.
    Thật đáng tiếc! bạn đã biến thành một con ếch.
    KẾT THÚC
    """, font=('', 20),align="center")

# THE MAIN PROGRAM
name = t.textinput("TÊN NGƯỜI CHƠI", "Bạn tên là gì?")
welcome_text = "CHÀO MỪNG " + str(name).upper() + " ĐẾN VỚI TRÒ CHƠI"
game_text = 'THÁM HIỂM KHU RỪNG BÍ ẨN'
ans = first_part()
if ans == "L":
    ans = left()
    if ans == "L":
        left_left()
        t.done()
    elif ans == "R":
        left_right()
        t.done()
elif ans == "R":
    ans = right()
    if ans == "L":
        right_left()
        t.done()
    elif ans == "R":
        right_right()
        t.done()
s.mainloop()
