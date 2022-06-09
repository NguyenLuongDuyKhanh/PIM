import tkinter as tk
import random
window = tk.Tk()
window.title('2048')
window.config(bg='azure3')

#tạo biến toàn cục
board = [] #chứa 4 list, mỗi list chứa 4 button => là mảng 2 chiều

#chia khung tạo bố cục
frame_label = tk.Frame(window, bg='azure3', padx=10, pady=10)
frame_label.pack(side='top')
frame_keys = tk.Frame(window, bg='azure3', padx=10, pady=10) #thứ tự code trước thì đặt sau trên màn hình
frame_keys.pack(side='top')
frame_board = tk.Frame(window, bg='#7a7877', padx=10, pady=10)
frame_board.pack(side='bottom')


#tạo tên trò chơi
label = tk.Label(frame_label, text = "Welcome to\n2048", font=("Arial Bold", 24), bg= '#F9F5F0', fg= '#b05b3b', width= 10, height=2)
label.pack(side='left', padx= 10, pady= 10)

#tạo bảng điểm
score_label = tk.Label(frame_label, text = "SCORE: 0", font=("Arial Bold", 15), bg= '#753422', fg='#F4DFBA')
score_label.pack(side='top', padx= 10, pady= 10)

#tạo nút New Game
new_game = tk.Button(frame_label, text = "NEW GAME", font=("Arial Bold", 12), bg= '#eec373', fg= '#5c3d2e', activebackground= '#f5e8c7')
new_game.pack(side='bottom', padx= 10, pady= 10)

#tạo bảng 4x4
for i in range(4):
    rows = []
    for j in range(4):
        l = tk.Label(frame_board, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
        l.grid(row=i, column=j, padx=7, pady=7)
        rows.append(l)
    board.append(rows)


#tạo bảng nút điều khiển
up_key = tk.Button(frame_keys, text="Up", font=('arial bold', 15), fg="red")
up_key.grid(row=0, column=1)
left_key = tk.Button(frame_keys, text="Left", font=('arial bold', 15), fg="brown")
left_key.grid(row=1, column=0)
down_key = tk.Button(frame_keys, text="Down", font=('arial bold', 15), fg="blue")
down_key.grid(row=1, column=1)
right_key = tk.Button(frame_keys, text="Right", font=('arial bold', 15), fg="purple")
right_key.grid(row=1, column=2)

window.mainloop()


