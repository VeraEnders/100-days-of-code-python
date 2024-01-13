# BMI Calculator 
# Write a program that calculates the Body Mass Index (BMI) from a user's
# weight and height.
# The BMI is calculated by dividing a person's weight by the square of their height.
# BMI = weight / (height ** 2)
# Example: weight = 80, height = 1.75 -> BMI = 26.122448979591837
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / (float(height) ** 2)
print("Your BMI is " + str(bmi))