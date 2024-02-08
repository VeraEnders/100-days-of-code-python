import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary
dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words
# from a word that the user inputs.
word = input("Enter a word: ")

result = [dict[letter.upper()] for letter in word]
print(result)
