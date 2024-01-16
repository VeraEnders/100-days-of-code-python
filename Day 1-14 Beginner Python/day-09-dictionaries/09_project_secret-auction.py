# Blind Auction

# Write a program that will collect the names and bids of different people. 
# The program should ask for each bidder's name and their bid individually.
# If there are other bidders, the screen should clear, so you can pass your phone to the next person.
# If there are no more bidders, then the program should display the name of the winner and their winning bid.

# Example output: The winner is Elon with a bid of $55000000000
import os

print("Welcome to the secret auction program. ")

bids = {}

while True:
  name_bidder = input("What is your name? ")
  bid = int(input("What's your bid? $"))

  bids[name_bidder] = bid

  is_end = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  os.system('cls')

  if is_end == 'no':
    winner = max(bids)
    max_bid = max(bids.values())
    print(f"The winner is {winner} with a bid of ${max_bid}")
    break