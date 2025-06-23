li = [1,2,3,4,5]
li2 = ['a', 'b', 'c', 'd']
li3 = [True, 0, 0.4, 'coffee']

amazon = ['notebooks', 'laptop', 'sunglasses', 'apples']
# List Indexing
print(amazon[1])
print(amazon[-2])

# List Slicing
print(amazon[1:])
print(amazon[-2:])
amazon[2] = 'grapes'
print(amazon)

new_cart = amazon[:3] # Made a copy of amazon list
print(new_cart)
print(amazon)
print()
new_cart[0] = 'mouse'
print(new_cart)
print(amazon)