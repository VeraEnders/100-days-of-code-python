# There is no Block Scope
if 3 > 2:
  a_variable = 10

############## Local Scope ##############
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
# potion_strength has local scope, accessing it outside the function causes an error
# print(potion_strength)

############## Global Scope ##############
player_health = 10

def drink_health():
  print(player_health)

drink_health()
print(player_health)

# Modifying Global Scope
enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Global Constants
# uppercased, separated with underscores

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@xyz"