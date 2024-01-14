import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)

# Create a variable 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives = 6

# Create an empty List called display with "_" for each letter in the chosen_word
display = ["_"] * len(chosen_word)

# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
def reveal_letter(guess, word):
  for i, letter in enumerate(word):
    if letter == guess:
      display[i] = letter

# Ask the user to guess a letter. Make guess lowercase.
# Use a while loop to let the user guess. The loop should only stop once the user has guessed 
# all the letters in the chosen_word. Then you can tell the user they've won.
while True:
  print(f"{' '.join(display)}")

  guess = input("Guess a letter: ").lower()

  if guess not in chosen_word:
    print("Not match")
    lives -= 1
    print(stages[lives + 1])

    if lives < 0:
      print("Game over. You lose.")
      break
  else:
    reveal_letter(guess, chosen_word)

  if not "_" in display:
    print(f"{' '.join(display)}")
    print("You win.")
    break