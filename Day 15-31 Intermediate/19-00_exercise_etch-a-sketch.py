# Etch-A-Sketch App

# Create a turtle object that moves in response to keyboard input:
# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
  timmy.forward(30)

def move_backwards():
  timmy.backward(30)
  
def turn_left():
  new_heading = timmy.heading() + 20
  timmy.setheading(new_heading)

def turn_right():
  new_heading = timmy.heading() - 20
  timmy.setheading(new_heading)

def clear():
  timmy.clear()
  timmy.penup()
  timmy.home()
  timmy.pendown()

screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()