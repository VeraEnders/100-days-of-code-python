# Write a program which will wark a spot with an X.
# The map is made of 3 rows of blank squares:
#     1    2    3
# 1 [' ', ' ', ' ']
# 2 [' ', ' ', ' ']
# 3 [' ', ' ', ' ']
# Your program should allow you to enter the position of the treasure using a two-digit system.
# The first digit is the horizontal column number.The second digit is the vertical row number.
# Example Input: 23 
# Example Output:
# [' ', ' ', ' ']
# [' ', ' ', ' ']
# [' ', 'X', ' ']

row1 = ['◼', '◼', '◼']
row2 = ['◼', '◼', '◼']
row3 = ['◼', '◼', '◼']
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

col_index = int(position[0]) - 1
row_index = int(position[1]) - 1
map[row_index][col_index] = '✖'

print(f"{row1}\n{row2}\n{row3}")