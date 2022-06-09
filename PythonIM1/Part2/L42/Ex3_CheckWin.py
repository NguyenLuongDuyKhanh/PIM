import tkinter
from tkinter import messagebox

screen = tkinter.Tk()
button_size = 150
screen.geometry("500x500")

def check_win():
    # Hang ngang
    if button_1["text"] == "O" and button_2["text"] == "O" and button_3["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X":
        messagebox.showinfo("", "X win")

    if button_4["text"] == "O" and button_5["text"] == "O" and button_6["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_4["text"] == "X" and button_5["text"] == "X" and button_6["text"] == "X":
        messagebox.showinfo("", "X win")

    if button_7["text"] == "O" and button_8["text"] == "O" and button_9["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_7["text"] == "X" and button_8["text"] == "X" and button_9["text"] == "X":
        messagebox.showinfo("", "X win")


    # Hang doc
    if button_1["text"] == "O" and button_4["text"] == "O" and button_7["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_1["text"] == "X" and button_4["text"] == "X" and button_7["text"] == "X":
        messagebox.showinfo("", "X win")

    if button_2["text"] == "O" and button_5["text"] == "O" and button_8["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_2["text"] == "X" and button_5["text"] == "X" and button_8["text"] == "X":
        messagebox.showinfo("", "X win")

    if button_3["text"] == "O" and button_6["text"] == "O" and button_9["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_3["text"] == "X" and button_6["text"] == "X" and button_9["text"] == "X":
        messagebox.showinfo("", "X win")


    # Duong cheo
    if button_1["text"] == "O" and button_5["text"] == "O" and button_9["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X":
        messagebox.showinfo("", "X win")

    if button_3["text"] == "O" and button_5["text"] == "O" and button_7["text"] == "O":
        messagebox.showinfo("", "O win")

    if button_3["text"] == "X" and button_5["text"] == "X" and button_7["text"] == "X":
        messagebox.showinfo("", "X win")


def cpu_move():
    # Di ngau nhien
    if button_5["text"] != "O" and button_5["text"] != "X":
        button_5["text"] = "X"
        return

    if button_1["text"] != "O" and button_1["text"] != "X":
        button_1["text"] = "X"
        return

    if button_3["text"] != "O" and button_3["text"] != "X":
        button_3["text"] = "X"
        return

    if button_7["text"] != "O" and button_7["text"] != "X":
        button_7["text"] = "X"
        return

    if button_9["text"] != "O" and button_9["text"] != "X":
        button_9["text"] = "X"
        return

    if button_2["text"] != "O" and button_2["text"] != "X":
        button_2["text"] = "X"
        return

    if button_4["text"] != "O" and button_4["text"] != "X":
        button_4["text"] = "X"
        return

    if button_6["text"] != "O" and button_6["text"] != "X":
        button_6["text"] = "X"
        return

    if button_8["text"] != "O" and button_8["text"] != "X":
        button_8["text"] = "X"
        return

def button_1_click():
    if button_1["text"] == "O":
        return
    if button_1["text"] == "X":
        return
    button_1["text"] = "O"
    cpu_move()

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
    cpu_move()

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
    cpu_move()

button_3= tkinter.Button(command=button_3_click)
button_3["text"] = "Hello"

button_3["bg"] = "blue"
button_3["activebackground"] = "white"

button_3["fg"] = "white"
button_3["activeforeground"] = "blue"

button_3.place(x=button_size * 2, y=0, width=button_size, height=button_size)

def button_4_click():
    if button_4["text"] == "O":
        return
    if button_4["text"] == "X":
        return
    button_4["text"] = "O"
    cpu_move()

button_4= tkinter.Button(command=button_4_click)
button_4["text"] = "Hello"

button_4["bg"] = "blue"
button_4["activebackground"] = "white"

button_4["fg"] = "white"
button_4["activeforeground"] = "blue"

button_4.place(x=0, y=button_size, width=button_size, height=button_size)

def button_5_click():
    if button_5["text"] == "O":
        return
    if button_5["text"] == "X":
        return
    button_5["text"] = "O"
    cpu_move()

button_5= tkinter.Button(command=button_5_click)
button_5["text"] = "Hello"

button_5["bg"] = "blue"
button_5["activebackground"] = "white"

button_5["fg"] = "white"
button_5["activeforeground"] = "blue"

button_5.place(x=button_size, y=button_size, width=button_size, height=button_size)

def button_6_click():
    if button_6["text"] == "O":
        return
    if button_6["text"] == "X":
        return
    button_6["text"] = "O"
    cpu_move()

button_6= tkinter.Button(command=button_6_click)
button_6["text"] = "Hello"

button_6["bg"] = "blue"
button_6["activebackground"] = "white"

button_6["fg"] = "white"
button_6["activeforeground"] = "blue"

button_6.place(x=button_size * 2, y=button_size, width=button_size, height=button_size)

def button_7_click():
    if button_7["text"] == "O":
        return
    if button_7["text"] == "X":
        return
    button_7["text"] = "O"
    cpu_move()

button_7= tkinter.Button(command=button_7_click)
button_7["text"] = "Hello"

button_7["bg"] = "blue"
button_7["activebackground"] = "white"

button_7["fg"] = "white"
button_7["activeforeground"] = "blue"

button_7.place(x=0, y=button_size * 2, width=button_size, height=button_size)

def button_8_click():
    if button_8["text"] == "O":
        return
    if button_8["text"] == "X":
        return
    button_8["text"] = "O"
    cpu_move()

button_8= tkinter.Button(command=button_8_click)
button_8["text"] = "Hello"

button_8["bg"] = "blue"
button_8["activebackground"] = "white"

button_8["fg"] = "white"
button_8["activeforeground"] = "blue"

button_8.place(x=button_size, y=button_size * 2, width=button_size, height=button_size)

def button_9_click():
    if button_9["text"] == "O":
        return
    if button_9["text"] == "X":
        return
    button_9["text"] = "O"
    cpu_move()

button_9= tkinter.Button(command=button_9_click)
button_9["text"] = "Hello"

button_9["bg"] = "blue"
button_9["activebackground"] = "white"

button_9["fg"] = "white"
button_9["activeforeground"] = "blue"

button_9.place(x=button_size * 2, y=button_size * 2, width=button_size, height=button_size)

screen.mainloop()