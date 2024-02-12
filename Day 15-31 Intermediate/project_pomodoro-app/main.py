from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global reps
  reps = 0
  window.after_cancel(timer)

  canvas.itemconfig(timer_text, text="00:00")
  title.config(text="Timer", fg=GREEN)
  # reset checkmarks
  checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if reps % 8 == 0:
    count_down(long_break_sec)
    title.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    count_down(short_break_sec)
    title.config(text="Break", fg=PINK)
  else:
    count_down(work_sec)
    title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

  count_min = math.floor(count / 60)
  if count_min < 10:
    count_min = f"0{count_min}"

  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    num_checkmarks = math.floor(reps / 2)
    text_checkmarks = "✔" * num_checkmarks
    checkmark.config(text=text_checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Title Label
title = Label(text="Timer", font=(FONT_NAME, 38, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

# Checkmarks
checkmark = Label(font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()