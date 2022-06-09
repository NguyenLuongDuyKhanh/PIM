import tkinter
window = tkinter.Tk()

btn_decrease = tkinter.Button(master=window, text="-")
btn_decrease.pack()

lbl_value = tkinter.Label(master=window, text="0")
lbl_value.pack()

btn_increase = tkinter.Button(master=window, text="+")
btn_increase.pack()

window.mainloop()