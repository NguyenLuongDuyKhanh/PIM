import tkinter
screen = tkinter.Tk()
screen.title('My Title')

label = tkinter.Label(
    text="Hello World!",
    foreground="white",  # Set the text color to white
    background="blue",  # Set the background color to black
    width=10,
    height=10,
)
label.pack()

screen.mainloop()