# Turtle Race Game

from turtle import Turtle, Screen
import tkinter as tk
from tkinter import messagebox
import random

# Constants
COLORS = ["red", "orange", "black", "green", "blue", "purple"]
NUM_TURTLES = len(COLORS)

WIDTH_SCREEN = 500
HEIGHT_SCREEN = 400
X_PADDING = 20
Y_PADDING = 100
X_START = -(WIDTH_SCREEN / 2 - X_PADDING)
Y_START = -(HEIGHT_SCREEN / 2 - Y_PADDING)

HALF_TURTLE  = 20
X_END = WIDTH_SCREEN / 2 - HALF_TURTLE

def create_turtles(num_turtles):
  """
    Creates a list of Turtle objects with specified colors.

    Parameters:
    - num_turtles (int): The number of turtles to create.

    Returns:
    - list: A list containing Turtle objects.
  """
  global X_START, Y_START

  all_turtles = []
  for i in range(num_turtles):
    turtle = Turtle(shape="turtle")
    turtle.color(COLORS[i])
    turtle.penup()
    turtle.goto(x=X_START, y=Y_START)
    Y_START += 40
    all_turtles.append(turtle)

  return all_turtles

# Function to display result
def display_result(winning_color, user_bet):
  """
    Displays a message box with the result of the turtle race.

    Parameters:
    - winning_color (str): The color of the winning turtle.
    - user_bet (str): The user's bet on the winning turtle's color.
  """
  if winning_color == user_bet:
    result = f"You win! The {winning_color} turtle is the winner."
  else:
    result = f"You lose. The {winning_color} turtle is the winner."

  messagebox.showinfo("Result", result)

# Main code
screen = Screen()
screen.setup(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)

list_of_turtles = create_turtles(NUM_TURTLES)

user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")
is_race_on = True

while is_race_on:
  for turtle in list_of_turtles:
    rand_dist = random.randint(0, 10)
    turtle.forward(rand_dist)

    if turtle.xcor() > X_END:
      is_race_on = False
      winning_color = turtle.pencolor()
      display_result(winning_color, user_bet)
        
screen.exitonclick()

