import turtle as t
import random

# Change the color mode
t.colormode(255)

def random_color():
  """Returns a random color using RGB."""
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

timmy = t.Turtle()
screen = t.Screen()

timmy.shape("turtle")
timmy.color(random_color())
timmy.forward(50)
timmy.right(90)

screen.resetscreen()

######################################################################
# # Draw a Square
for _ in range(4):
  timmy.forward(50)
  timmy.left(90)

screen.resetscreen()

######################################################################
# Draw a Dashed Line
for _ in range(15):
  timmy.forward(10)
  timmy.penup()
  timmy.forward(10)
  timmy.pendown()

screen.resetscreen()

######################################################################
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
MAX_NUM_OF_SIDES = 10
number_of_sides = 3

while number_of_sides <= MAX_NUM_OF_SIDES:
  angle = 360 / number_of_sides
  timmy.speed("fastest")
  timmy.pencolor(random_color())
  for _ in range(number_of_sides):
    timmy.forward(70)
    timmy.right(angle)

  number_of_sides += 1

screen.resetscreen()

######################################################################
# Draw a Random Walk
DIRECTIONS = [0, 90, 180, 270]

screen.screensize(2000,1500)

for _ in range(50):
  steps = int(random.random() * 100)
  direction = random.choice(DIRECTIONS)

  timmy.speed("fastest")
  timmy.width(5)
  timmy.pencolor(random_color())
  timmy.forward(steps)
  timmy.setheading(direction)

screen.resetscreen()

######################################################################
# Draw a Spirograph
circles = 50

for _ in range(circles):
  angle = 360 / circles

  timmy.speed("fastest")
  timmy.pencolor(random_color())
  timmy.circle(100)
  timmy.left(angle)

screen.exitonclick()