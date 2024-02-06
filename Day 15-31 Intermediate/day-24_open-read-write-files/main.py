# Read the file

## Opening and closing the file
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Open the file in read mode
with open("my_file.txt") as file:
  contents = file.read()
  print(contents)

# Write data in the file in write mode
with open("new_file.txt", mode="w") as file:
  file.write("New text.")

# Append data in the file
with open("new_file.txt", mode="a") as file:
  file.write("\nAdd new text.")