import tkinter
screen = tkinter.Tk()
screen.title('My Title')

def click():
    print('Button was clicked!')

button = tkinter.Button(
    text="Click me!",
    width=25,
    height=5,
    bd=20,
    bg="blue",
    fg="yellow",
    activebackground='black',
    activeforeground='white',
    command=click
)

button["activebackground"]='white'
button["activeforeground"]='black'

button.pack()

screen.mainloop()