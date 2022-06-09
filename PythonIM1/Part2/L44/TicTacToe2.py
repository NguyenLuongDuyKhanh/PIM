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

def button_player1(button):
    '''This function is used to change the style of button after clicking for X'''
    button.update()
    button['fg'] = 'yellow'
    button['text'] = 'X'
    button['bg'] = 'blue'

def button_player2(button):
    '''This function is used to change the style of button after clicking for player O'''
    button.update()
    button['fg'] = 'yellow'
    button['text'] = 'O'
    button['bg'] = 'red'

def update_board(position,button):
    global turn
    print(stop_list)
    # Player 1 turns of even number
    if turn%2==0:
        # Updates the player turn label on the window
        turn_indicator.update()
        turn_indicator['text'] = 'Turn: Player 2'
        if board[position-1] == '-': # condition for checking the position by player is empty or not. '-' refers to empty
            button.update()
            button_player1(button) # Calling the button style change function when it is clicked
            board[position-1] = 'X' # Updating postion on board
            turn += 1
        else: # Show error if positon is not empty
            msg.showinfo('Eroor!',"Please don't try to overite the position..")

    # Odd refers for second player
    elif turn%2!=0:
        # updating the player indicator label
        turn_indicator.update()
        turn_indicator['text'] = 'Turn: Player 1'
        if board[position-1]=='-':# condition for checking the position by player is empty or not. '-' refers to empty
            button.update()
            print('player 2 turn')
            button_player2(button)# Calling the button style change function when it is clicked
            board[position-1] = 'O' # updating the position on board in backend
            turn += 1
        else:
            msg.showinfo('Eroor!',"Please don't try to overite the position..")

# The styling of window starts from here
Label(root,text='Welcome in Tic Tac Toe Game',font='Arial 25 bold',fg='black',bg='orange').pack(pady=4)

turn_indicator = Label(root,text='Turn: Player 1',font='MVBoli 19 bold')
turn_indicator.pack()
# First Frame
f1 = Frame(root,width=450,height=100,bg='yellow')
f1.pack(pady=10)
b1 = Button(f1,text=board[0],width=3,font='Arial 48 bold',bg='black',fg='white',relief=GROOVE,bd=4,command=lambda :update_board(1,b1))
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