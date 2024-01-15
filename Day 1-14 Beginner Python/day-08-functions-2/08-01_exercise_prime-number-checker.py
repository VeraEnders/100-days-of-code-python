# Prime Number Checker

# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# Write a function that checks whether if the number passed into it is a prime number or not.
# 73 is a prime number. 75 is not a prime number.
import math

def is_number_prime(num):
  if num == 1 or num == 2: return True
  half = math.ceil(num / 2)
  for i in range(3, half + 1):
    if num % i == 0:
      return False
    
  return True

number = int(input("Type a whole number: "))
print(f"{number} is {'not ' if not is_number_prime(number) else ''}a prime number.")