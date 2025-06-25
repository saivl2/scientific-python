basket = [1,2,3,4,5]

# Adding items
basket.append(100)

print(basket)

basket.insert(3, 'tea')
print(basket)

basket.extend(['sunglasses', 'grapes', 'bottles'])
print(basket)

# Removing items

basket.pop() # Removes the last item of the list
print(basket)

basket.pop(1) # Pass in the index
print(basket)

basket.remove('sunglasses') # Pass in the value
print(basket)

# basket.clear()
# print(basket)

# Where is the value 3?
print(basket.index(3))

print('coffee' in basket)

print(basket.count('bottles'))

# Sorting
basket = [34, 67, 21, 90, -45]
basket.sort() # Sorts in-place
print(basket)

# Returns the sorted list
sorted_list = sorted(basket)
print(sorted_list)

basket.reverse()
print(basket)