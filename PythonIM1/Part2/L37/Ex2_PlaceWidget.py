import tkinter
screen = tkinter.Tk()
screen.title('My Title')

label = tkinter.Label(text="Hello World!")
label.place(x=100, y=100)
button = tkinter.Button(text="Hi")
button.place(x=0, y=0)

screen.mainloop()