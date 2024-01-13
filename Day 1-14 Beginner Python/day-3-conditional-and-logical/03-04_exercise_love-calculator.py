# Write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# Example Input: name1 = "Angela Yu", name2 = "Jack Bauer"
# T occurs 0 times. R occurs 1 time. U occurs 2 times. E occurs 2 times. Total = 5
# L occurs 1 time. O occurs 0 times. V occurs 0 times. E occurs 2 times. Total = 3
# Love Score = 53
# Output: Print: "Your score is 53."

# Example Input 1: name1 = "Kanye West", name2 = "Kim Kardashian". 
# Output: Your score is 42, you are alright together.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined = name1 + name2
combined_lower = combined.lower()

total_true = 0
total_love = 0

def count_letters(word, letter):
  return word.count(letter)

for char in "true":
  total_true += count_letters(combined_lower, char)

for char in "love":
  total_love += count_letters(combined_lower, char)

total_score = int(str(total_true) + str(total_love))

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")