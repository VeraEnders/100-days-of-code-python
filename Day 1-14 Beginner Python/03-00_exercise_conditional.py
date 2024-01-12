# Write a program that works out whether if a given number is an odd or even number.
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is a even number.")
else:
  print("This is an odd number.")

# Write a program that asks a user for their height and age and then prints a message.
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print("You can ride the rollercoaster!")

  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print(f"Child tickets are ${bill}.")
  elif age <=18:
    bill = 7
    print(f"Youth tickets are ${bill}.")
  else:
    bill = 12
    print(f"Adult tickets are ${bill}.")
  
  wants_photo = input("Do you want a photo taken (Y / N): ")
  if wants_photo == "Y":
    # Add $3 to their bill
    bill += 3

  print(f"Your final bill is {bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

