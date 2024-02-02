from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.print_score()
   
  def print_score(self):
    self.penup()
    self.goto(0, 270)
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.print_score()

  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write(f"GAME OVER.\nTotal score: {self.score}.", align=ALIGNMENT, font=FONT)
