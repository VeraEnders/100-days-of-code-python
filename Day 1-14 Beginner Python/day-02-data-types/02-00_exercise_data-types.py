# Data Types
print(type(123))

# String
print("Hello"[0])
print(len("Hello"))
print("123" + "345")

# Integer
print(123 + 456)

# Float
pi = 3.14159

# Boolean
True
False

# Type conversion
num_char = len(input("what is your name? "))
print("Your name has " + str(num_char) + " characters.")

print(str(80) + str(100))
print(12 + float(100.5))

# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8
num_user = input("Type a two digit number: ")

first_digit = int(num_user[0])
second_digit = int(num_user[1])
result = first_digit + second_digit
print(f"{first_digit} + {second_digit} = {result}")

# Mathematical Operations
print(6 / 3)
print(2 ** 3)

# f-String
score = 0
height_m = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height_m}. You are winning is {isWinning}!")

