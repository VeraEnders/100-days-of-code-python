# Password Generator

# The program will ask:
# How many letters would you like in your password?
# How many symbols would you like?
# How many numbers would you like?
# The objective is to take the inputs from the user to these questions and then generate a random password. 
# Every time you generate a password, the positions of the symbols, numbers, and letters are different.

import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

selected_chars = []

def select_random(length, list):
  result = []
  for i in range(0, length):
    random_char = random.choice(list)
    result.append(random_char)
  return result

selected_chars.extend(select_random(nr_letters, letters))
selected_chars.extend(select_random(nr_symbols, symbols))
selected_chars.extend(select_random(nr_numbers, numbers))

random.shuffle(selected_chars)
password = "".join(selected_chars)

print(f"Here is your password: {password}")
