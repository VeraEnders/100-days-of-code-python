# Rock Paper Scissors

# The "official" rules of the game on the World Rock Paper Scissors Association website:
# https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
# Make a rock, paper, scissors game.
# Start the game by asking the player: "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(f"You chose: {game_images[user_choice]}")
  print(f"Computer chose: {game_images[computer_choice]}")

  if user_choice == computer_choice:
    print("It's a draw.")
  elif (user_choice == 0 and computer_choice == 2) or (user_choice > computer_choice):
    print("You win.")
  else:
    print("You lose.")


