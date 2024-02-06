# Taks: Create a letter using starting_letter.txt for each name in invited_persons.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "readyToSend"

# Get names
with open("./input/names/invited_persons.txt") as file:
  names = file.readlines()

# Get the text of the letter template
with open("./input/letters/starting_letter.txt") as template:
  text = template.read()

for name in names:
  # Remove spaces from the name:
  updated_name = name.strip("\n")
  
  # replace [name] in the letter template with the actual name
  updated_text = text.replace("[name]", updated_name)

  # Create a new letter with the name
  letter_file_name = f"letter_for_{updated_name}"
  with open(f"./output/readyToSend/{letter_file_name}.txt", mode="w") as letter:
    letter.write(updated_text)
