import tkinter as tk

window = tk.Tk()
frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
label1 = tk.Label(master=window, text="Row 0\n Column 0")
label1.grid(row=0, column=0)

label2 = tk.Label(master=window, text="Row 0\n Column 1")
label2.grid(row=0, column=1)

label3 = tk.Label(master=window, text="Row 0\n Column 2")
label3.grid(row=0, column=2)

label4 = tk.Label(master=window, text="Row 1\n Column 0")
label4.grid(row=1, column=0)

label5 = tk.Label(master=window, text="Row 1\n Column 1")
label5.grid(row=1, column=1)

label6 = tk.Label(master=window, text="Row 1\n Column 2")
label6.grid(row=1, column=2)

label7 = tk.Label(master=window, text="Row 2\n Column 0")
label7.grid(row=2, column=0)

label8 = tk.Label(master=window, text="Row 2\n Column 1")
label8.grid(row=2, column=1)

label9 = tk.Label(master=window, text="Row 2\n Column 2")
label9.grid(row=2, column=2)
window.mainloop()