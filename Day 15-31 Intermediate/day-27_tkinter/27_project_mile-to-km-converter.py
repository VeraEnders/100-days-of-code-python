from tkinter import *

def miles_to_km():
  miles = miles_input.get()
  km = 1.609 * float(miles)
  km_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

# Entry
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=0, row=0)

# Miles Label 
label_miles = Label()
label_miles.config(text="Miles is equal to")
label_miles.grid(column=1, row=0)

# Km Result Label
km_result_label = Label(text="0")
km_result_label.grid(column=2, row=0)

# Km Label
label_km = Label()
label_km.config(text="Km")
label_km.grid(column=3, row=0)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=1)

window.mainloop()