from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Lables
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email / Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=50)
entry_website.grid(column=1, row=1, columnspan=3)
entry_website.focus()

entry_email = Entry(width=50)
entry_email.grid(column=1, row=2, columnspan=3)
entry_email.insert(0, "email@email.com")

entry_password = Entry(width=32)
entry_password.grid(column=1, row=3)

# Buttons
button_password = Button(text="Generate Password")
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=43)
button_add.grid(column=1, row=4, columnspan=3)

window.mainloop()