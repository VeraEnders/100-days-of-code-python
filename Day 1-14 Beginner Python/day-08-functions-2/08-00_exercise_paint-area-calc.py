# You are painting a wall. The instructions on the paint can says
# that 1 can of pain can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint
# you'll need to buy. The result should be rounded up to a whole number.

# num_cans = (wall_height * wall_width) / coverage_per_can
# Example input: height = 2, width = 4, coverage = 5. Output: num_cans = 2
import math

def paint_calc(height, width, coverage_per_can):
  result = (height * width) / coverage_per_can
  return math.ceil(result)

wall_height = float(input("Height of wall: "))
wall_width = float(input("Width of wall: "))

coverage = 5
num_cans = paint_calc(wall_height, wall_width, coverage)
print(f"You should buy {num_cans} cans.")
