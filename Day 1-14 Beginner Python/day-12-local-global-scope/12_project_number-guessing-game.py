# Number Guessing Game

import random

# Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer):
  """Checks user's guess against actual answer."""
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  elif difficulty == 'hard':
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  # Choosing a random number between 1 and 100
  answer = random.randint(1, 100)

  # Choosing a difficulty of the game
  turns = set_difficulty()
  print(f"You have {turns} attempts remaining to guess the number.")

  while turns > 0:
    # Let the user guess a number
    guess = int(input("Make a guess: "))
    check_answer(guess, answer)

    if guess == answer: 
      break
    else:
      turns -= 1
      print(f"You have {turns} attempts remaining to guess the number.")

  if turns == 0:
    print("You've run out of guesses. You lose.")

game()