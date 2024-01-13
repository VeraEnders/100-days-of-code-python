fruits = ['apple', 'banana', 'apricot', 'kiwi']
print(fruits)

print(fruits[1])

# the last item in the list
print(fruits[-1])

# change items
fruits[1] = 'peach'
print(fruits)

# add an item to the end of the list
fruits.append('mango')
print(fruits)

# add all items of the list to the list
fruits.extend(['lemon', 'grapes', 'plum'])
print(fruits)

# nested lists
vegetables = ['spinach', 'kale', 'tomato', 'celery', 'potato' ]
fruits_vegetables = [fruits, vegetables]
print(fruits_vegetables)