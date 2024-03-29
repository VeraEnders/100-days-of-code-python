# Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small Pizza: $15 | Medium Pizza: $20 | Large Pizza: $25
# Pepperoni for Small Pizza: +$2 | Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input: size = "L", add_pepperoni = "Y", extra_cheese = "N"
# Example Output: Your final bill is: $28.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

price_pizza = [15, 20, 25]
price_extra_pepperoni = [2, 3]
price_extra_cheese = 1

bill = 0

if size == 'S':
  bill += price_pizza[0]
elif size == 'M':
  bill += price_pizza[1]
else:
  bill += price_pizza[2]

if add_pepperoni == 'Y':
  if size == 'S':
    bill += price_extra_pepperoni[0]
  else:
    bill += price_extra_pepperoni[1]

if extra_cheese == 'Y':
  bill += price_extra_cheese

print(f"Your final bill is: ${bill}.")