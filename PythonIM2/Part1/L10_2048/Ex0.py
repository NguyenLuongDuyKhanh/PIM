import tkinter as tk
window = tk.Tk()
window.title('2048')
window.config(bg='azure3')
#chia khung tạo bố cục
frame_label = tk.Frame(window, width=600, height=100, bg='azure3',
padx=10, pady=10)
frame_label.pack(side='top')
frame_board = tk.Frame(window, width=500, height=500,
bg='#7a7877', padx=10, pady=10)
frame_board.pack(side='top')
#tạo tên trò chơi
label = tk.Label(frame_label, text = "Welcome to\n2048",
font=("Arial Bold", 24), bg= '#F9F5F0', fg= '#b05b3b', width= 10,
height=2)
label.pack(side='left', padx= 10, pady= 10)

#tạo bảng điểm
score_label = tk.Label(frame_label, text = "SCORE: 0",
font=("Arial Bold", 15), bg= '#753422', fg='#F4DFBA')
score_label.pack(side='top', padx= 10, pady= 10)

#tạo nút New Game
new_game = tk.Button(frame_label, text = "NEW GAME", font=("ArialBold", 12), bg= '#eec373', fg= '#5c3d2e', activebackground='#f5e8c7')
new_game.pack(side='bottom', padx= 10, pady= 10)
board = [] #chứa 4 list, mỗi list chứa 4 button
#tạo bảng 4x4
for i in range(4):
    rows = []
    for j in range(4):
        l = tk.Label(frame_board, text='', bg='azure4',
        font=('arial', 22, 'bold'), width=4, height=2)
        l.grid(row=i, column=j, padx=7, pady=7)
        rows.append(l)
    board.append(rows)

window.mainloop()