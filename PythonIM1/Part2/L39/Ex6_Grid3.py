import tkinter as tk

window = tk.Tk()
frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
for i in range(3):
    for j in range(3):
        label = tk.Label(master=window, text=f"Row {i}\nColumn {j}")
        label.grid(row=i, column=j)

window.mainloop()