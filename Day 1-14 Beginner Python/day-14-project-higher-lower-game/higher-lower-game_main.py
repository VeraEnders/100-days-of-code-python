# The Higher Lower Game

import random
from data import data

score = 0

def format_data(person):
  """Format the person data into printable format."""
  name = person['name']
  desc = person['description']
  country = person['country']
  return f"{name}, a {desc}, from {country}"

def game(score):
  # Choose two random celebrities from provided data.
  person_1 = random.choice(data)
  person_2 = random.choice(data)
  if person_1 == person_2:
    person_2 = random.choice(data)

  followers_1, followers_2 = person_1['follower_count'], person_2['follower_count']

  if followers_1 > followers_2:
    answer = 'A'
  else:
    answer = 'B'
    
  print(f"Compare A: {format_data(person_1)}.")
  print(f"Compare B: {format_data(person_2)}.")
  user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  if user_answer == answer:
    score += 1
    
  return score 

while True:
  current_score = game(score)
  if current_score != score:
    score = current_score
    print(f"You're right! Current score: {score}.")
    print("'(っ◕‿◕)っ '")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    break