import tkinter
window = tkinter.Tk()

def increase():
    print("Tang bien dem")


def decrease():
    print("Giam bien dem")


btn_decrease = tkinter.Button(master=window, text="-", command=decrease)
btn_decrease.pack()

lbl_value = tkinter.Label(master=window, text="0")
lbl_value.pack()

btn_increase = tkinter.Button(master=window, text="+", command=increase)
btn_increase.pack()

window.mainloop()