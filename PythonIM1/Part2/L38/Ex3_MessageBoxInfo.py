import tkinter
from tkinter import messagebox

screen = tkinter.Tk()

label = tkinter.Label(text="Hello World!")
label.pack()

messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")

screen.mainloop()
