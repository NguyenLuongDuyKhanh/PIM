
from tkinter import *
import tkinter.messagebox as msg
# Setting up window
root = Tk()
root.geometry('500x550')
root.maxsize(500,550)
root.minsize(500,550)
# Some variables Defined
turn = 2 # For acucessig the player turn. if it is even then player 1 and odd player2
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
stop_list =[] # list for stopping whenever game is winned the stop is appended in this list
root.config(bg='yellow')



def update_board(position,button):
    print("Update")
    pass

# The styling of window starts from here
Label(root,text='Welcome in Tic Tac Toe Game',font='Arial 25 bold',fg='black',bg='orange').pack(pady=4)

turn_indicator = Label(root,text='Turn: Player 1',font='MVBoli 19 bold')
turn_indicator.pack()
# First Frame
f1 = Frame(root,width=450,height=100,bg='yellow')
f1.pack(pady=10)
b1 = Button(f1,text=board[0],width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda: update_board(1,b1))
b1.pack(side=LEFT,padx=4)
b2 = Button(f1,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(2,b2))
b2.pack(side=LEFT,padx=4)
b3 = Button(f1,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(3,b3))
b3.pack()
# Second frame
f2 = Frame(root,width=450,height=100,bg='yellow')
f2.pack(pady=10)
b4 = Button(f2,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(4,b4))
b4.pack(side=LEFT,padx=4)
b5 = Button(f2,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(5,b5))
b5.pack(side=LEFT,padx=4)
b6 = Button(f2,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(6,b6))
b6.pack()
# Third frame
f3 = Frame(root,width=450,height=100,bg='yellow')
f3.pack(pady=10)
b7 = Button(f3,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(7,b7))
b7.pack(side=LEFT,padx=4)
b8 = Button(f3,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(8,b8))
b8.pack(side=LEFT,padx=4)
b9 = Button(f3,text='-',width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(9,b9))
b9.pack()

root.mainloop()