import tkinter as tk
import random
from tkinter import messagebox
window = tk.Tk()
window.title('2048')
window.config(bg='azure3')
#tạo bảng màu
bg_color = {
        0: 'azure4',
        2: '#eee4da',
        4: '#ede0c8',
        8: '#fabb46',
        16: '#eda53f',
        32: '#fa9146',
        64: '#f65e3b',
        128: '#edcf72',
        256: '#edcc61',
        512: '#f2b179',
        1024: '#f59563',
        2048: '#edc22e',
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
        512: '#776e65',
        1024: '#573202',
        2048: '#261600',
    }

board = []
value = []
score = 0

def can_move():
    """
    Kiểm tra xem còn ô trống nào trên bàn cờ không
    """
    global value
    for i in range(4):
        for j in range(4):
            if value[i][j] == 0:
                return True
    return False

def random_number():
    global board, value
    if can_move() == True: #kiểm tra xem bàn cờ còn ô trống để sinh số hay không
        r = random.randrange(0, 4) #chỉ số hàng
        c = random.randrange(0, 4) #chỉ số cột
        while value[r][c] != 0:
            r = random.randrange(0, 4)
            c = random.randrange(0, 4)

        num = random.choice([2, 4]) #giá trị
        board[r][c].config(text= str(num), bg= bg_color[num], fg= color[num])
        value[r][c] = num

#chia khung tạo bố cục
frame_label = tk.Frame(window, bg='azure3', padx=10, pady=10)
frame_label.pack(side='top')
frame_board = tk.Frame(window, bg='#7a7877', padx=10, pady=10)
frame_board.pack(side='top')
frame_keys = tk.Frame(window, bg='azure3', padx=10, pady=10)
frame_keys.pack(side='bottom')


#tạo bảng 4x4
for i in range(4):
    rows = []
    for j in range(4):
        l = tk.Label(frame_board, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
        l.grid(row=i, column=j, padx=7, pady=7)
        rows.append(l)
    board.append(rows)

#tạo giá trị 0 cho ma trận value
for i in range(4):
    value.append([0] * 4)

def compress():
    """
    Dồn số theo chiều từ phải sang trái
    """
    global value
    for i in range(4):
        pos = 0
        if value[i] == [0, 0, 0, 0]: #nếu dòng toàn số 0 thì không cần dồn số
            continue
        while pos < 4:
            while pos < 4 and value[i][pos] != 0: #tìm vị trí trống đầu tiên
                pos += 1
            if pos == 4 or (pos == 3 and value[i][pos] != 0): #nếu dòng đã full hoặc còn trống 1 ô cuối thì k cần compress nữa
                break
            for j in range(pos+1, 4): #tìm vị trí khác 0 đầu tiên ở dằng sau để dồn
                if value[i][j] != 0:
                    value[i][pos], value[i][j] = value[i][j], value[i][pos] #hoán đổi giá trị cho nhau
                    break #chỉ dồn 1 số duy nhất để tránh việc đằng sau còn nhiều số nữa
            pos += 1

def merge():
    """
    Cộng 2 ô liên tiếp giống nhau (theo chiều từ phải sang trái)
    """
    global value
    for i in range(4):
        for j in range(3):
            if value[i][j] == value[i][j+1] and value[i][j] != 0:
                value[i][j] = value[i][j] * 2
                value[i][j + 1] = 0

def refill():
    """
    Cập nhật lại text ở các ô
    """
    global value
    for i in range(4):
        for j in range(4):
            new_value = value[i][j]
            if new_value <= 2048: #nếu những con số nhỏ hơn 2048 thì dùng bảng màu 2048
                board[i][j].config(text= str(new_value),
                    bg= bg_color[new_value],
                    fg= color[new_value])
            else:
                board[i][j].config(text=str(new_value), bg=bg_color[2048], fg=color[2048])

def reverse():
    """
    Đảo ngược thứ tự của một mảng
    """
    global value
    for i in range(4):
        left = 0
        right = 3
        while (left < right):
            value[i][left], value[i][right] = value[i][right], value[i][left]
            left += 1
            right -= 1

def transpose():
    """
    Chuyển vị ma trận
    """
    for i in range(4):
        for j in range(i):
            for ..
            value[i][j], value[j][i] = value[j][i], value[i][j]

def can_merge():
    """
    Kiểm tra xem còn có thể cộng dồn lại được không
    """
    global value
    for i in range(4): #kiểm tra theo hàng
        for j in range(3):
            if value[i][j] == value[i][j + 1]:
                return True

    for i in range(3): #kiểm tra theo cột
        for j in range(4):
            if value[i + 1][j] == value[i][j]:
                return True
    return False

def end_game():
    """
    Kiểm tra xem thắng hay thua hay còn tiếp tục chơi được
    """
    global score
    # kiểm tra thắng
    if score == 2048:
        choose = messagebox.askyesno("2048", message="You win!!!\nDo you want to continue?")
        if choose == False:
            reset()

    #kiểm tra thua
    if (can_move() == False) and (can_merge() == False):
        messagebox.showinfo("2048", message="You lose!!!")
        reset()

def update_score():
    global score, score_label
    max = 0
    for i in range(4):
        for j in range(4):
            if max < value[i][j]:
                max = value[i][j]
    if max != score: #nếu khác điểm cũ thì mới cập nhật lại
        score = max
        score_label.config(text="SCORE: " + str(score))

def reset():
    for i in range(4):
        for j in range(4):
            value[i][j] = 0
    refill()
    random_number()

def left(event=None):
    compress()
    merge()
    compress()
    refill()
    update_score()
    random_number()
    end_game()

def right(event=None):
    reverse()
    compress()
    merge()
    compress()
    reverse()
    refill()
    update_score()
    random_number()
    end_game()

def up(event=None):
    transpose()
    compress()
    merge()
    compress()
    transpose()
    refill()
    update_score()
    random_number()
    end_game()

def down(event=None):
    transpose()
    reverse()
    compress()
    merge()
    compress()
    reverse()
    transpose()
    refill()
    update_score()
    random_number()
    end_game()

window.bind( '<Left>', left)
window.bind( '<Right>', right)
window.bind( '<Up>', up)
window.bind( '<Down>', down)

#tạo tên trò chơi
label = tk.Label(frame_label, text = "Welcome to\n2048", font=("Arial Bold", 24), bg= '#F9F5F0', fg= '#b05b3b', width= 10, height=2)
label.pack(side='left', padx= 10, pady= 10)

#tạo bảng điểm
score_label = tk.Label(frame_label, text = "SCORE: 0", font=("Arial Bold", 15), bg= '#753422', fg='#F4DFBA')
score_label.pack(side='top', padx= 10, pady= 10)

#tạo nút New Game
new_game = tk.Button(frame_label, text = "NEW GAME", font=("Arial Bold", 12), bg= '#eec373', fg= '#5c3d2e', activebackground= '#f5e8c7', command= reset)
new_game.pack(side='bottom', padx= 10, pady= 10)

#tạo bảng nút điều khiển
up_key = tk.Button(frame_keys, text="Up", font=('arial bold', 15), fg="red", command= up)
up_key.grid(row=0, column=1)
left_key = tk.Button(frame_keys, text="Left", font=('arial bold', 15), fg="brown", command= left)
left_key.grid(row=1, column=0)
down_key = tk.Button(frame_keys, text="Down", font=('arial bold', 15), fg="blue", command= down)
down_key.grid(row=1, column=1)
right_key = tk.Button(frame_keys, text="Right", font=('arial bold', 15), fg="purple", command= right)
right_key.grid(row=1, column=2)

random_number()
update_score()

window.mainloop()

