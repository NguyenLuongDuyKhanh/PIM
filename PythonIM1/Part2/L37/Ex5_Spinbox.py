import tkinter

screen = tkinter.Tk()
screen.geometry('400x200')
def HelloFunction():
    print("Hello")
def display_selected():
    msg.config(
        text=f'You selected {var.get()}',
        font=('sans-serif', 14),
        bg='#D97904'
        )

var = tkinter.StringVar()
tkinter.Spinbox(
    master=screen,
    value=['Grapes', 'Banana', 'Mango', 'Blueberries'],
    textvariable=var,
    command=display_selected,
).pack()

msg = tkinter.Label(
    screen,
    text='',
    bg='#D97904'
)
msg.pack()

w1 = tkinter.Spinbox(
    master=screen,
    from_=0,
    to=10,
    command=HelloFunction
)

w1.pack()

screen.mainloop()