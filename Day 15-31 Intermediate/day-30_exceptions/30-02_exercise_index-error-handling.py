# # We've got some buggy code, try running the code.

# fruits = ["Apple", "Banana", "Pear"]
# def make_pie(index):
#   fruit = fruits[index]
#   print(fruit + " pie")

# make_pie(4)

# # The code will crash and give you an IndexError.
# # Prevent the program from crashing. If the user enters something that is out of range
# # print a default output of "Fruit pie".

fruits = ["Apple", "Banana", "Pear"]
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie.")
  else:
    print(fruit + " pie")

make_pie(4)