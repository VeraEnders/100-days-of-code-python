# Highest Score

# Write a program that calculates the highest score from a List of scores.
# Important you are not allowed to use the max or min functions.
# Example Input: 78 65 89 86 55 91 64 89. Output: The highest score in the class is: 91.

student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = student_scores[0]
for i in range(1, len(student_scores)):
  if student_scores[i] > highest_score:
    highest_score = student_scores[i]

print(f"The highest score in the class is: {highest_score}.")