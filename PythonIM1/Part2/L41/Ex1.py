import tkinter
from tkinter import messagebox

screen = tkinter.Tk()
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