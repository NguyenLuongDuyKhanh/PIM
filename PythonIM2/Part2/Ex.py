import tkinter
import random
from tkinter import messagebox
from tkinter import ttk
screen = tkinter.Tk()
screen.title('Hi')
screen.config(bg='black')

board = []
value = []

bg_color = {
        0: 'azure4',
        2: '#eee4da',
        4: '#ede0c8',
        8: '#fabb46',
        16: '#eda53f',
        32: '#fa9146',
        64: '#edcf72',
        128: '#edcc61',
        256: '#edcc61',
        512: '#f2b179',
        1028: '#f59563',
        2048: '#edc22e'
    }
color = {
        0: 'azure4',
        2: '#776e65',
        4: '#785E4D',
        8: '#f9f6f2',
        16: '#f9f6f2',
        32: '#f9f6f2',
            64: '#f9f6f2',
        128: '#f9f6f2',
        256: '#f9f6f2',
        521: '#776e65',
        1028: '#573202',
        2048: '#261600'
    }

def print_size():
    welcomecs.pack_forget()
    choose_size.pack_forget()
    choose_target.pack_forget()
    buton.pack_forget()
    size.pack_forget()
    target.pack_forget()
    sp()

list_size = [2,3,4,5]
target_size = [1024, 2048, 4096]

welcomecs = tkinter.Label(
    text = 'Welcome to 2048',
    font = ('', 30),
    bg = 'orange'
)

size = tkinter.Label(
    text = 'Choose the size:',
    font = ('', 15)
)

target = tkinter.Label(
    text = 'Choose the target:',
    font = ('', 15)
)

choose_size = ttk.Combobox(
    master = screen,
    values = list_size,
)
choose_target = ttk.Combobox(
    master = screen,
    values = target_size,
)

buton = tkinter.Button(
    text = 'Start the game',
    master = screen,
    command = print_size
)

welcomecs.pack(side = 'top')
size.pack(side = 'top', padx = 8, pady = 8, expand = True, fill = 'both')
choose_size.pack(side = 'top', expand = True)
target.pack(side = 'top', padx = 10, pady = 10, expand = True, fill = 'both')
choose_target.pack(side = 'top', expand = True)
buton.pack(side = 'bottom', padx = 10, pady = 10, expand = True)

def randomn():
    global board, value

    if canmove() == True:
        c = random.randrange(0, 4)
        r = random.randrange(0, 4)

    while value[r][c] != 0:
        c = random.randrange(0, 4)
        r = random.randrange(0, 4)

    num = random.choice([2, 4])
    board[r][c].config(text = str(num))
    value[r][c] = num

def canmove():
    otrong = True

    for x in range(4):
        for y in range(4):
            if value[x][y] == 0:
                otrong = False
    if otrong == False:
        return True
    else:
        return False

def compress():
    global value
    for i in range(4):
        pos = 0
        if value[i] == [0, 0, 0, 0]:
            continue
        while pos < 4:
            while pos < 4 and value[i][pos] != 0:
                pos += 1
            if pos == 4 or (pos == 3 and value[i][pos] != 0):
                break
                for j in range(pos+1, 4):
                    if value[i][j] != 0:
                        value[i][pos], value[i][j] = value[i][j], value[i][pos]
                        break
            pos += 1
def merge():
    global value
    for i in range(4):
        for j in range(3):
            if value[i][j] == value[i][j+1] and value[i][j] != 0:
                value[i][j] = value[i][j] * 2
                value[i][j+1] = 0

def refill():
    global board

    for i in range(4):
        for j in range(4):
            newv = value[i][j]
            if newv <= 2048:
                board[i][j].config(text = str(newv), bg = bg_color[newv], fg = color[newv])
            else:
                board[i][j].config(text = str(newv), bg = bg_color[2048], fg = color[2048])

def reverse():
    global value

    for i in range(4):
        left = 0
        right = 3
        while (left<right):
            value[i][left], value[i][right] = value[i][right], value[i][left]
            right -= 1
            left += 1

def transpose():
    global value
    for i in range(4):
        for j in range(i):
            if i > j:
                value[i][j], value[j][i] = value[j][i], value[i][j]
            if i == j:
                break

def can_merge():
    global value

    for i in range(4):
        for j in range(3):
                if value[i][j] == value[i] [j + 1]:
                    return True
    for i in range(3):
        for j in range(4):
            if value[i][j] == value[i + 1] [j]:
                return True
    return False

def end_game():
    win = False
    for x in range(4):
        for y in range(4):
            if value[x][y] == 2048:
                win = True
                break

    if win == True:
        messagebox.showinfo("2048", "You Win")
        res_askokcancel = messagebox.askokcancel("ask ok cancel", "Want to countinue")

        if res_askokcancel == True:
            print("User choice ok")
        if res_askokcancel == False:
            print("User choice cancel")

    if can_merge() == False and canmove() == False:
        print('ko merge duoc')
        messagebox.showinfo('2048', 'You lose')
        reset()

def reset(event = None):
    for x in range(4):
        for y in range(4):
            value[x][y] = 0
    Point['text'] = 'Point: '
    refill()

def update_score():
    solonnhat = 0
    for x in range(4):
        for y in range(4):
            while value[x][y] > solonnhat:
                solonnhat = value[x][y]

    Point['text'] = 'Point : ' + str(solonnhat)

def left(event = None):
    compress()
    merge()
    compress()
    refill()
    update_score()
    randomn()
    end_game()
def right(event = None):
    reverse()
    compress()
    merge()
    compress()
    reverse()
    refill()
    update_score()
    randomn()
    end_game()
def up(event = None):
    transpose()
    compress()
    merge()
    compress()
    transpose()
    refill()
    update_score()
    randomn()
    end_game()
def down(event = None):
    transpose()
    reverse()
    compress()
    merge()
    compress()
    reverse()
    transpose()
    refill()
    update_score()
    randomn()
    end_game()

screen.bind('<Left>', left)
screen.bind('<Right>', right)
screen.bind('<Up>', up)
screen.bind('<Down>', down)
screen.bind('e', reset)

def sp():
    screen.title('2048')
    screen.geometry("400x700")

    frame = tkinter.Frame(master = screen, width = 300, height = 100, bg = 'black')
    frame.pack()

    welcome = tkinter.Label(
        bg = 'gray',
        master = frame,
        text = 'Welcome to 2048', font = ('', 15)
    )
    welcome.place(x = 20, y = 40)

    Point = tkinter.Label(
        bg = 'white',
        master = frame,
        text = 'Point:', font = ('', 10),
    )
    Point.place(x = 200, y = 20)

    Newgame = tkinter.Button(
        bg = 'white',
        master = frame,
        text = 'New Game ', font = ('', 10),
        command = reset
    )
    Newgame.place(x = 200, y = 50)

    frame2 = tkinter.Frame(master = screen, width = 400, height = 300, bg = 'black')
    frame2.pack()

    for rows in range(4):
        row = []
        for columns in range(4):
            holes = tkinter.Label(
                master = frame2,
                bg = 'gray',
                width = 10,
                height = 5
            )
            holes.grid(row = rows, column = columns, padx = 10, pady = 10)
            row.append(holes)
        board.append(row)

    for rows in range(4):
        value.append([0] * 4)

    frame3 = tkinter.Frame(master = screen, width = 500, height = 300, bg = 'black')
    frame3.pack()

    Up = tkinter.Button(
        bg = 'white',
        master = frame3,
        text = 'Up', font = ('', 10),
        width = 5,
        height = 3,
        command = up
    )
    Up.place(x = 180, y = 20)

    Down = tkinter.Button(
        bg = 'white',
        master = frame3,
        text = 'Down', font = ('', 10),
        width = 5,
        height = 3,
    )
    Down.place(x = 180, y = 90)

    Right = tkinter.Button(
        bg = 'white',
        master = frame3,
        text = 'Right', font = ('', 10),
        width = 5,
        height = 3,
        command = right
    )
    Right.place(x = 240, y = 90)

    Left = tkinter.Button(
        bg = 'white',
        master = frame3,
        text = 'Left', font = ('', 10),
        width = 5,
        height = 3,
        command = left
    )
    Left.place(x = 120, y = 90)

screen.mainloop()


