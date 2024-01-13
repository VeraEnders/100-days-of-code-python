import random

# randint() method returns a number between num1 and num2 (both included):
random_int = random.randint(1, 10)
print(random_int)

# random float from 0.000000 to 0.9999999...
random_float = random.random()
print(random_float)

# random float from 0 to 4.99999...
random_float_0_to_5 = random_float * 5

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised e.g. Heads, not heads.
# You should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# e.g. 1 means Heads 0 means Tails
random_side = random.randint(0, 1)
if random_side == 0:
  print("Tails")
else:
  print("Heads")