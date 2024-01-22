# Blackjack Project

# Our Blackjack House Rules
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from blackjack_art import logo



def deal_card(created_list):
  """Adds a randomly chosen card from the deck to the provided list."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  created_list.append(random_card)
  return created_list

def calculate_score(cards_in_game):
  """Take a list of cards and return the score calculated from the cards."""
  score = sum(cards_in_game)
  
  if (11 in cards_in_game) and score < 21:
    index = cards_in_game.index(11)
    cards_in_game[index] = 1
    score = calculate_score(cards_in_game)
  return score

def game():
  user_cards = []
  computer_cards = []

  for _ in range(0, 2):
    deal_card(user_cards)
    deal_card(computer_cards)

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  while True:
    if (user_score > 21 or computer_score == 21) or (computer_score > 21 or user_score == 21):
      break
    else:
      print(f"Your cards: {user_cards}. Your score is {user_score}.")
      print(f"Computer's cards: {computer_cards}. Computer's score is {computer_score}.")
      next_card = input("Do you want to draw another card? (y / n): ").lower()
      if next_card == 'y':
        user_cards = deal_card(user_cards)
        user_score = calculate_score(user_cards)
      elif next_card == 'n':
        while computer_score < 17:
          computer_cards = deal_card(computer_cards)
          computer_score = calculate_score(computer_cards)
        break
      else:
        print("Incorrect input. Please type 'y' or 'n'. ")

  print(f"Your cards: {user_cards}. Your score is {user_score}.")
  print(f"Computer's cards: {computer_cards}. Computer's score is {computer_score}.")

  if user_score == computer_score:
    print("It's a draw.")
  elif user_score > 21 or computer_score == 21 or (user_score < 21 and computer_score < 21 and user_score < computer_score):
    print("Game over. You lose.")
  elif computer_score > 21 or user_score == 21 or (computer_score < 21 and computer_score < user_score):
    print("You win.")

while True: 
  print(logo)
  game()

  new_game = input("Do you want to restart the game? Type 'y' or 'n': ").lower()

  if new_game == 'y':
    os.system('cls')
  elif new_game == 'n':
    print("Goodbye.")
    break
  else:
    print("Incorrect input. Please type 'y' or 'n'. ")