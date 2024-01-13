# Average Height
# Write a program that calculates the average student height from a List of heights.
# Average height should be round to the nearest whole number. 
# Example Input: 156 178 165 171 187. # Output: 171

student_heights = input("Input a list of student heights: ").split()
num_of_students = len(student_heights)
total_height = 0

for n in range(0, num_of_students):
  student_heights[n] = int(student_heights[n])
  total_height += student_heights[n]

avg_height = round(total_height / num_of_students)
print(f"Average student height is {avg_height}.")