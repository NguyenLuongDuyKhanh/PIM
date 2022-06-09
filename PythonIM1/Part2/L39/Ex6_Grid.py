import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(
    master=window,
    relief=tkinter.RAISED,
    borderwidth=1
)
frame.pack()
button1 = tkinter.Button(
    master = frame,
    text="Button 1",
)
button1.grid(row=1, column=1)

button2 = tkinter.Button(
    master = frame,
    text="Button 2",
)
button2.grid(row=2, column=2)

window.mainloop()