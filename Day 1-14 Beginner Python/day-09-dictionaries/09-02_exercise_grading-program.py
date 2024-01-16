# Grading program
# You have access to a database of student_scores in the format of a dictionary.
# The keys are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades.
# Do not modify the existing student_scores dictionary.
# You should create a new dictionary called student_grades.
# This is the scoring criteria:
# Scores 91-100: Grade = "Outstanding"
# Scores 81-90: Grade = "Exceeds Expectations"
# Scores 71-80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

def score_to_grade(score):
  if score >= 91: 
    return "Outstanding"
  elif score >= 81 and score <= 90: 
    return "Exceeds Expectations"
  elif score >= 71 and score <= 80: 
    return "Acceptable"
  else: 
    return "Fail"

for key in student_scores:
  student_grades[key] = score_to_grade(student_scores[key])

print(student_grades)