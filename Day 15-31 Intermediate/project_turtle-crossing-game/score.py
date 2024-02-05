from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.level = 1
    self.print_level()

  def print_level(self):
    self.clear()
    self.goto(-280, 250)
    self.write(f"Level: {self.level}", align="left", font=FONT)

  def update_level(self):
    self.level += 1
    self.print_level()

  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write(f"GAME OVER", align="center", font=FONT)