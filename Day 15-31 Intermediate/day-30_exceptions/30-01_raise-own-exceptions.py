height = float(input("Height in m: "))
weight = int(input("Weight in kg: "))

if height > 3:
  raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)