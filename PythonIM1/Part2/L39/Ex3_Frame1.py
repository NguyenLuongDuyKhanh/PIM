import tkinter

screen = tkinter.Tk()

frame_l = tkinter.Frame(
    master=screen,
)
frame_l.pack(side=tkinter.LEFT)

label_l = tkinter.Label(
    master=frame_l,
    text='Left'
)
label_l.pack()

frame_r = tkinter.Frame(
    master=screen,
)
frame_r.pack(side=tkinter.RIGHT)

label_r = tkinter.Label(
    master=frame_r,
    text='Right'
)
label_r.pack()