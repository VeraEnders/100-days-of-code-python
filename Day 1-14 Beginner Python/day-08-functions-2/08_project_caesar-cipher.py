# Caesar cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  result = ""
  shift %= len(alphabet) 

  if direction == "decode": 
    shift *= -1
    
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      position_new = (position + shift) % len(alphabet)
      result += alphabet[position_new]
    else:
      result += char
  
  return result

while True:
  while True:
    direction_user = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction_user not in ['encode', 'decode']:
      print("Please type 'encode' or 'decode'\n")
    else:
      break

  text_user = input("Type your message:\n").lower()
  shift_user = int(input("Type the shift number:\n"))

  print(f"The {direction_user}d text is '{caesar(direction_user, text_user, shift_user)}'")
  end = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

  if end == 'no':
    print("Goodbye.")
    break
