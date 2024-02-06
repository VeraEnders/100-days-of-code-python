from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.print_score()
   
  def print_score(self):    
    self.clear()
    self.write(f"Score: {self.score}. High score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.print_score()

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0
    self.print_score()

  # def game_over(self):
  #   self.clear()
  #   self.goto(0, 0)
  #   self.write(f"GAME OVER.\nTotal score: {self.score}.", align=ALIGNMENT, font=FONT)
