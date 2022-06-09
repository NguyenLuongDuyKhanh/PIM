import tkinter
from tkinter import messagebox

screen = tkinter.Tk()
screen.geometry("500x200")
button_size = 150

def button_1_click():
    if button_1["text"] == "O":
        return
    if button_1["text"] == "X":
        return
    button_1["text"] = "O"

button_1 = tkinter.Button(command=button_1_click)
button_1["text"] = "Hello"

button_1["bg"] = "blue"
button_1["activebackground"] = "white"

button_1["fg"] = "white"
button_1["activeforeground"] = "blue"

button_1.place(x=0, y=0, width=button_size, height=button_size)

def button_2_click():
    if button_2["text"] == "O":
        return
    if button_2["text"] == "X":
        return
    button_2["text"] = "O"


button_2= tkinter.Button(command=button_2_click)
button_2["text"] = "Hello"

button_2["bg"] = "blue"
button_2["activebackground"] = "white"

button_2["fg"] = "white"
button_2["activeforeground"] = "blue"

button_2.place(x=button_size, y=0, width=button_size, height=button_size)

def button_3_click():
    if button_3["text"] == "O":
        return
    if button_3["text"] == "X":
        return

    button_3["text"] = "O"

button_3= tkinter.Button(command=button_3_click)
button_3["text"] = "Hello"

button_3["bg"] = "blue"
button_3["activebackground"] = "white"

button_3["fg"] = "white"
button_3["activeforeground"] = "blue"

button_3.place(x=button_size * 2, y=0, width=button_size, height=button_size)

screen.mainloop()