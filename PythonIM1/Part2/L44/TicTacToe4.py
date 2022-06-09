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
root.config(bg='yellow')

def display_board():
    '''The function is used to draw board'''
    print(board[0] + ' | ' + board[1] + ' | ' +board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_winner():
    '''The function used to check winner'''
    # Checking rows
    if board[0] == board[1] == board[2] and board[0]!= '-':
        msg.showinfo('Winner','Congratulations ' + board[0] + '.....\n Well played ')
        print(board[0], ' is winner')
        clear_list_and_reset_button_text()
    elif board[3] == board[4] ==board[5] and board[3]!= '-':
        msg.showinfo('Winner','Congratulations ' + board[3] + '.....\n Well played ')
        print(board[3], ' is winner')
        clear_list_and_reset_button_text()
    elif board[6] == board[7] ==board[8] and board[6]!= '-':
        msg.showinfo('Winner','Congratulations ' + board[6] + '.....\n Well played ')
        print(board[6], ' is winner')
        clear_list_and_reset_button_text()

    # Checking Columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i]!='-':
            msg.showinfo('Winner','Congratulations ' + board[i] + '.....\n Well played ')
            print(board[i], ' is winnner')
            clear_list_and_reset_button_text()

    # For diagonals
    if ((board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])) and board[4]!='-':
        msg.showinfo('Winner','Congratulations ' + board[4] + '.....\n Well played ')
        print(board[4],' is winner')
        clear_list_and_reset_button_text()

def check_tie():
    ''''Function for check match is tie or not.'''
    if '-' not in board :# len()==0 means stop not in list or '-' not in board means all the
        print('The match is tie')
        msg.showinfo('Tie','Ohh!....The match is tie')

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

def reset_button_style(button):
    '''This fuction will clear all the effects on button when game restart'''
    button.update()
    button['fg'] = 'white'
    button['text'] = '-'
    button['bg'] = 'black'


def clear_list_and_reset_button_text():
    '''This function is used to play game again by setting all the variables to its initial position'''
    # This function will ran only when someone win or game is tie
    button_list = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in range(9):
        reset_button_style(button_list[i]) # Reseting the style of all buttons
        board[i] = '-' # Setting board again
    print(board)
    turn_indicator.update()
    turn_indicator['text']= 'Turn: Player 1' # initially turn is first player



def update_board(position,button):
    global turn
    print(turn)
    # Player 1 turns of even number
    if turn%2==0:
        # Updates the player turn label on the window
        turn_indicator.update()
        turn_indicator['text'] = 'Turn: Player 2'
        if board[position-1] == '-': # condition for checking the position by player is empty or not. '-' refers to empty
            button.update()
            button_player1(button) # Calling the button style change function when it is clicked
            board[position-1] = 'X' # Updating postion on board
            check_winner() # After every click checking for winner
            check_tie() # After every click checking for tie
            turn += 1
        else: # Show error if positon is not empty
            msg.showinfo('Eroor!',"Please don't try to overite the position..")

    # Odd refers for second player
    elif turn%2!=0:
        # updating the player indicator label
        turn_indicator.update()
        turn_indicator['text'] = 'Turn: Player 1'
        if board[position-1]=='-':# condition for checking the position by player is empty or not. '-' refers to empty
            print('player 2 turn')
            button_player2(button)# Calling the button style change function when it is clicked
            board[position-1] = 'O' # updating the position on board in backend
            check_winner() # checking for winner if any one wins then this function will add stop in a list
            check_tie() # checking for the tie
            # checking for stop or tie
            turn+=1
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