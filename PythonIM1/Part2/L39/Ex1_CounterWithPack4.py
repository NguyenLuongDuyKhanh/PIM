import tkinter
window = tkinter.Tk()
BienDem = 0
def increase():
    global BienDem
    BienDem += 1
    #lbl_value["text"] = BienDem

def decrease():
    global BienDem
    BienDem -= 1
    #lbl_value["text"] = BienDem

btn_decrease = tkinter.Button(master=window, text="-", command=decrease)
btn_decrease.pack()

lbl_value = tkinter.Label(master=window, text="0")
lbl_value.pack()

btn_increase = tkinter.Button(master=window, text="+", command=increase)
btn_increase.pack()

window.mainloop()