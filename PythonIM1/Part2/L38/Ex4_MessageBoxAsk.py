import tkinter
from tkinter import messagebox

screen = tkinter.Tk()

label = tkinter.Label(text="Hello World!")
label.pack()

res_askquestion = messagebox.askquestion("askquestion", "Are you sure?")
if res_askquestion == 'yes':
    print('User chose Yes')
elif res_askquestion == 'no':
    print('User chose No')

res_askokcancel = messagebox.askokcancel("askokcancel", "Want to continue?")
if res_askokcancel == True:
    print('User chose OK')
elif res_askokcancel == False:
    print('User chose Cancel')

res_askyesno = messagebox.askyesno("askyesno", "Find the value?")
if res_askyesno == True:
    print('User chose Yes')
elif res_askyesno == False:
    print('User chose No')

res_askyesno = messagebox.askretrycancel("askretrycancel", "Try again?")
if res_askyesno == True:
    print('User chose Retry')
elif res_askyesno == False:
    print('User chose Cancel')

screen.mainloop()
