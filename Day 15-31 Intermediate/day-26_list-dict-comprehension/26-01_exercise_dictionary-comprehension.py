import random

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_score = {name:random.randint(1,100) for name in names}
print(student_score)

passed_students = {name:score for (name, score) in student_score.items() if score >= 55}
print(passed_students)

# Task 1
# Create a dictionary that takes each word in the given sentence
# and calculates the number of letters in each word.
# Use Dict Comprehension instead of a Loop.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()

result = {word:len(word) for word in words}
print(result)

# Task 2
# Create a dictionary that takes each temperature in degrees Celcius
# and converts it into degrees Farenheight.
# To convert temp_c into temp_f: temp_f = (temp_c * 9/5) + 32
weather_c = {
  "Monday": 12,
  "Tuesday": 14,
  "Wednesday": 15,
  "Thursday": 14,
  "Friday": 21,
  "Saturday": 22,
  "Sunday": 24
}

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)