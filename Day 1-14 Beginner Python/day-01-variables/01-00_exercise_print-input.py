print('Hello world!')

# New line
print('Hello world!\nHello world!')

# String concatenation
print('Hello' + ' ' + 'Jane')

# input
input('What is your name? ')
print('Hello' + ' ' + input('What is your name? '))

# prints the number of characters in a user's name
user_name = input('What is your name? ')
length_name = len(user_name)
print(length_name)

# Write a program that switches the values stored in the variables a and b.
a = input('a: ')
b = input('b: ')

a, b = b, a

print('a = ' + a)
print('b = ' + b)