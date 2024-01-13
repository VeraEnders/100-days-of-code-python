# Who's Paying

# Write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.

# Example Input: Angela, Ben, Jenny, Michael, Chloe
# Example Output: Michael is going to buy the meal today!

import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

# person_who_will_pay = random.choice(names)
rand_name_index = random.randrange(0, len(names))
person_who_will_pay = names[rand_name_index]
print(f"{person_who_will_pay} is going to buy the meal today!")

