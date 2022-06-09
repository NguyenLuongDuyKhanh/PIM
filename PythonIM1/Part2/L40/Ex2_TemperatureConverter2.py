import tkinter


# Set-up the window
window = tkinter.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tkinter.Frame(master=window)
ent_temperature = tkinter.Entry(master=frm_entry, width=10)
lbl_temp = tkinter.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

frm_entry.pack()
# Run the application
window.mainloop()