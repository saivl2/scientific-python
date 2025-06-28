my_tuple = (1,2,3,4,5,1,1)

print(my_tuple[3])
print(6 in my_tuple)

# Tuple Tricks
new_tuple = my_tuple[1:4]
print(new_tuple)

x, y, *other = my_tuple
print(x)
print(y)
print(other)

# Tuple Methods

print(my_tuple.count(1))
print(my_tuple.index(2))
print(len(my_tuple))