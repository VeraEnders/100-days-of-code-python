# Task 1
# Create a new list which contains every number in the list `number`
# Each number should be squared.
# Output: [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

# Task 2
# Create a new list which contains the even numbers from thhe list `numbers`
# Output: [2, 8, 34]

result = [n for n in numbers if n % 2 == 0]
print(result)

# Task 3
# Create a list which contains the numbers that are common in both lists.
# Try to use List Comprehension instead of Loop.
# Output: [3, 6, 5, 33, 12, 7, 42, 13]

list_1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
list_2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]

common_numbers = [n for n in list_1 if n in list_2]
print(common_numbers)