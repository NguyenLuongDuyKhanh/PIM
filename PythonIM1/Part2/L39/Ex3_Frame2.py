import tkinter

screen = tkinter.Tk()

#FLAT, SUNKEN, RAISED, GROOVE, RIDGE

frame_l = tkinter.Frame(
    master=screen,
    relief=tkinter.SUNKEN,
    borderwidth=5
)
frame_l.pack(side=tkinter.LEFT)
label_l = tkinter.Label(
    master=frame_l,
    text='Left'
)
label_l.pack()

frame_r = tkinter.Frame(
    master=screen,
    relief=tkinter.RAISED,
    borderwidth=5
)
frame_r.pack(side=tkinter.RIGHT)
label_r = tkinter.Label(
    master=frame_r,
    text='Right'
)
label_r.pack()