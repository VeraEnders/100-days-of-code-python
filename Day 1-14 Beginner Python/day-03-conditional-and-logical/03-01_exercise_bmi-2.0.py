# Write a program that interprets the BMI based on a user's weight and height.
# It should tell them the interpretation of their BMI:
# under 18.5 - underweight
# over 18.5 but below 25 - normal weight
# over 25 but below 30 - overweight
# over 30 but below 35 - obese
# above 35 - clinically obese.
# You should round the result to the nearest whole number.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
  print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}. You are a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}. You are obese.")
else:
  print(f"Your BMI is {bmi}. You are clinically obese.")