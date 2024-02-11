import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
my_label = tkinter.Label(text="Label", font=("Arial", 20, "bold"))
# my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
def button_clicked():
  print("I got clicked")
  message = entry.get()
  my_label.config(text=message)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
entry = tkinter.Entry(width=30)
# Add some text to begin with
entry.insert(tkinter.END, string="Some text to begin with.")
entry.grid(column=2, row=1)

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Add some text to begin with
text.insert(tkinter.END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.grid(column=0, row=3)

# Spinbox
def spinbox_used():
  print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=1, row=3)

# Scale
# Called with current scale value
def scale_used(value):
  print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.grid(column=0, row=4)

# Checkbutton
def checkbutton_used():
  # prints 1 if On button checked, otherwise 0
  print(checked_state.get())
# Variable to hold on to checked state, 0 is off, 1 is on
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=1, row=4)

# Radiobutton
def radio_used():
  print(radio_state.get())
# Variable to hold on to which radio button value is checked
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=2, row=4)
radiobutton2.grid(column=2, row=4)

# Listbox
def listbox_used(event):
  # Gets current selection from listbox
  print(listbox.get(listbox.curselection()))
listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
  listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=0, row=5)

window.mainloop()