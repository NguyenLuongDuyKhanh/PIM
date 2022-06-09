import tkinter

screen = tkinter.Tk()

def TinhToan():
    KetQua = int(SoHang1.get()) + int(SoHang2.get())
    label['text']= "= " + str(KetQua)
    SoHang1.delete(0,tkinter.END)
    SoHang2.delete(0,tkinter.END)

SoHang1 = tkinter.Entry(
    fg="red",
    bg="white",
    width=20
)
SoHang1.pack()
SoHang2 = tkinter.Entry(
    fg="red",
    bg="white",
    width=20
)
SoHang2.pack()
button = tkinter.Button(
    text="Tinh Toan",
    command=TinhToan
)
button.pack()

label = tkinter.Label(text="Ket Qua")
label.pack()

screen.mainloop()