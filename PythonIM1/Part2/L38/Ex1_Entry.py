import tkinter
screen = tkinter.Tk()

def HamChucNang():
    print(entry.get())

entry = tkinter.Entry(
    fg="red",
    bg="white",
    width=50
)
entry.pack()

button = tkinter.Button(command=HamChucNang)
button.pack()

screen.mainloop()