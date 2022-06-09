import tkinter
import random
from tkinter import ttk
from tkinter import messagebox

screen = tkinter.Tk()
screen.title("2048")
screen.config(bg="azure3")
screen.geometry('500x600')

def first_page():
    label = tkinter.Label(
        master = screen,
        text = 'Welcome to 2048',
        font = 'Times 24 bold',
        width = 13,
        height = 2,
        foreground = 'White',
        background = 'Brown'
    )
    label.pack()

    label_size = tkinter.Label(master = screen, text = "Choose size of board")
    label_size.pack(padx = 10, pady = 10)


    list_size = [2,3,4,5]
    target_size = [1024,2048,4096]
    target = 0
    size = 0

    choose_size = ttk.Combobox(
        master = screen,
        values = list_size
    )
    choose_size.pack()

    label_target = tkinter.Label(master = screen, text = "Choose target score")
    label_target.pack(padx = 10, pady = 10)

    choose_target = ttk.Combobox(
        master = screen,
        values = target_size
    )
    choose_target.pack()

    def print_size(event = None):
        size = int(choose_size.get())
        target = int(choose_target.get())
        print(size)
        choose_target.pack_forget()
        choose_size.pack_forget()
        label_size.pack_forget()
        label_target.pack_forget()
        label.pack_forget()
        button_size.pack_forget()
        second_page()
        control()

    button_size = tkinter.Button(
        master = screen,
        text = "Start",
        font = 'Times 20 bold',
        bg = "Brown",
        fg = "White",
        command = print_size
    )
    button_size.pack(padx = 10, pady = 10)


def second_page():
    f1 = tkinter.Frame(
        master = screen
    )
    f1.pack(side="top",pady =10)
    label = tkinter.Label(
        master = f1,
        text = 'Welcome to \n2046',
        font = 'Times 24 bold',
        width = 10,
        height = 2,
        foreground = 'Red',
        background = 'White'
    )
    label.pack(side=tkinter.LEFT,padx = 10,pady = 10)

    score_label = tkinter.Label(
        master = f1,
        text = 'SCORE : 0',
        #width = 5,
        #bd = 5,
        font = 'Times 15 bold',
        foreground = 'yellow',
        background = 'brown'
    )
    score_label.pack(side=tkinter.TOP,padx = 10,pady = 10)

    f2 = tkinter.Frame(
        master = screen,
        bg = 'gray',
        width = 500,
        height = 500
    )
    f2.pack(pady = 20)
    board = []
    value = []

    for row in range(4):
        rows = []
        for column in range(4):
            label = tkinter.Label(
                master = f2,
                text='',
                bg='azure4',
                font = ('arial',22,'bold'),
                width=4,
                height=2
            )
            label.grid(row=row, column=column, padx=7, pady=7)
            rows.append(label)
        board.append(rows)

    for i in range(4):
        value.append([0] * 4)



    new_game_label = tkinter.Button(
        master = f1,
        text = 'NEW GAME',
        font = 'Times 12 bold',
        foreground = 'black',
        background = 'yellow'
    )
    new_game_label.pack(side=tkinter.BOTTOM,padx = 10,pady = 10)



first_page()
def control():
    f3 = tkinter.Frame(
    master = screen,
    bg = 'azure3',
    width = 500,
    height = 500
    )
    f3.pack(side='bottom',pady = 5)
    up_label = tkinter.Button(
    master = f3,
    text = 'UP',
    fg='Red',
    font = ('Arial',15),
    )
    up_label.grid(row = 1, column = 2)

    left_label = tkinter.Button(
    master = f3,
    text = 'LEFT',
    fg = 'Brown',
    font = ('Arial',15),
    )
    left_label.grid(row = 2, column = 1)

    down_label = tkinter.Button(
    master = f3,
    text = 'DOWN',
    fg = 'Blue',
    font = ('Arial',15,''),
    )
    down_label.grid(row = 2, column = 2)

    right_label = tkinter.Button(
    master = f3,
    text = 'RIGHT',
    fg = 'Purple',
    font = ('Arial',15),
    )
    right_label.grid(row = 2, column = 3)

def random_number():
    global board,value
    if can_move() == True:
        r = random.randrange(0,4)
        c = random.randrange(0,4)
        while value[r][c] !=0 :
            r = random.randrange(0,4)
            c = random.randrange(0,4)
        random_number = random.choice([2,4])
        board[r][c].config(text = str(random_number))
        value[r][c] = random_number
        for x in bg_color:
            if random_number == x:
                board[r][c].config(bg = bg_color[x])
                board[r][c].config(fg=color[x])


def reset():
    for x in range(4):
        for y in range(4):
            value[x][y]= 0
    refill()
    random_number()

