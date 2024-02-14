# # Catching exceptions
# try:      Something that might cause an exception
# except:   Do this if there was an exception
# else:     Do this if there were no exceptions
# finally:  Do this no matter what happens

# # FileNotFound
# with open("file.txt") as file:
#   file.read()
try:
  with open("file.txt") as file:
    file.read()
except FileNotFoundError:
  print("There was an error.")
else:
  content = file.read()
  print(content)
finally:
  print("File was closed.")

# # KeyError
# dict = {"key": "value"}
# value = dict["non_existent_key"]
try:
  dict = {"key": "value"}
  print(dict["non_existent_key"])
except KeyError as error_message:
  print(f"That key {error_message} does not exist.")
finally:
  raise TypeError("This is an error that I made up.")

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)