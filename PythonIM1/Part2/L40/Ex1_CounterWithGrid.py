import tkinter

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tkinter.Tk()


btn_decrease = tkinter.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tkinter.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tkinter.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()