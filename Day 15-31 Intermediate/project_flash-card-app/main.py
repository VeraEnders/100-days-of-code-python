import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA ------------------------------- #
data = pandas.read_csv("data/czech_words.csv")
list_data = data.to_dict(orient="records")

current_card = {}

# ---------------------------- PICK WORD ------------------------------- #
def next_word():
  global current_card, flip_timer
  window.after_cancel(flip_timer)

  current_card = random.choice(list_data)
  canvas.itemconfig(card_title, text="Czech", fill="black")
  canvas.itemconfig(card_word, text=current_card["Czech"], fill="black")
  canvas.itemconfig(card_img, image=card_front_img)

  flip_timer = window.after(3000, func=flip_card)

# ------------------------- REMOVE WORD FROM LIST ---------------------- #
def is_known():
  list_data.remove(current_card)
  print(len(list_data))
  next_word()

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
  global current_card
  canvas.itemconfig(card_title, text="English", fill="white")
  canvas.itemconfig(card_word, text=current_card["English"], fill="white")
  canvas.itemconfig(card_img, image=card_back_img)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Image
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)

# Words
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_btn = tkinter.Button(image=wrong_img, highlightthickness=0, command=next_word)

right_img = tkinter.PhotoImage(file="images/right.png")
right_btn = tkinter.Button(image=right_img, highlightthickness=0, command=is_known)

wrong_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

next_word()

window.mainloop()