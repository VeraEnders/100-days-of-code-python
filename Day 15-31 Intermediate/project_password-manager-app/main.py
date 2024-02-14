from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  entry_password.delete(0, END)

  random_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
  random_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
  random_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]
  
  password_list = random_letters + random_symbols + random_numbers
  random.shuffle(password_list)
  password = "".join(password_list)

  entry_password.insert(0, string=password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = entry_website.get()
  email = entry_email.get()
  password = entry_password.get()

  new_data = {
    website: {
      "email": email,
      "password": password,
    }
  }

  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
  else:
    try:
      with open("data.json", "r") as data_file:
        # Reading existing data
        data = json.load(data_file)
    except FileNotFoundError:
      # Creating new file
      with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=2)
    else:
      # Updating data with new data
      data.update(new_data)

      with open("data.json", "w") as data_file:
        # Saving updated data
        json.dump(data, data_file, indent=2)
    finally:
      entry_website.delete(0, "end")
      entry_password.delete(0, "end")

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
button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=43, command=save)
button_add.grid(column=1, row=4, columnspan=3)

window.mainloop()