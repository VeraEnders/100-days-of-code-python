import random
import turtle as t
from colors import list_rbg_colors

draw_obj = t.Turtle()
screen = t.Screen()

DOT_SIZE = 20
DIST_BETWEEN_DOTS = 50
NUM_OF_DOTS = 10
SCREEN_PADDING = 50

screen_size= DOT_SIZE * NUM_OF_DOTS + (NUM_OF_DOTS / 2 * DIST_BETWEEN_DOTS) + SCREEN_PADDING * 2

# Calculate the coordinates
x_min = -SCREEN_PADDING
y_min = -SCREEN_PADDING
x_max = x_min + screen_size
y_max = y_min + screen_size

screen.setup(screen_size, screen_size)
screen.setworldcoordinates(x_min, y_min, x_max, y_max)

# Set background color of the screen
screen.bgcolor("floral white")

screen.colormode(255)
draw_obj.speed("fastest")

for row in range(NUM_OF_DOTS):
  for _ in range(NUM_OF_DOTS):
    color = random.choice(list_rbg_colors)
    draw_obj.dot(DOT_SIZE, color)
    draw_obj.penup()
    draw_obj.forward(DIST_BETWEEN_DOTS)
    draw_obj.pendown()

  draw_obj.penup()
  draw_obj.setposition(0, DIST_BETWEEN_DOTS * (row + 1))

screen.exitonclick()