from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain

    self.window = Tk()
    self.window.title("Quizzler App")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    # Score
    self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 14, "bold"))
    self.score_label.grid(row=0, column=1)

    # Question
    self.canvas = Canvas(width=300, height=250)
    self.question_text = self.canvas.create_text(
      150, 
      125,
      width=280,
      text="Some Question Text", 
      fill=THEME_COLOR,
      font=("Arial", 14, "italic")
    )
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    # Buttons
    true_btn_img = PhotoImage(file="./images/true.png")
    self.true_btn = Button(image=true_btn_img, highlightthickness=0, command=self.pressed_true)
    self.true_btn.grid(row=2, column=0)

    false_btn_img = PhotoImage(file="./images/false.png")
    self.false_btn = Button(image=false_btn_img, highlightthickness=0, command=self.pressed_false)
    self.false_btn.grid(row=2, column=1)

    self.get_next_question()

    self.window.mainloop()
  
  def get_next_question(self):
    self.canvas.config(bg="white")
    self.score_label.config(text=f"Score: {self.quiz.score}")
    if self.quiz.still_has_questions():
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text=q_text)
    else:
      self.canvas.itemconfig(self.question_text, text=f"Done!\nYour score: {self.quiz.score}")
      self.true_btn.config(state="disabled")
      self.false_btn.config(state="disabled")

  def pressed_false(self):
    is_right = self.quiz.check_answer("False")
    self.give_feedback(is_right)

  def pressed_true(self):
    is_right = self.quiz.check_answer("True")
    self.give_feedback(is_right)

  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)

