#fix this code so that it prints a sorted list of all of our friends (alphabetical). 
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.extend(new_friend)
friends.sort()
print(friends)

# .join()

l1 = ['a', 'b', 'c', 'd']
new_l = ''.join(l1)
print(new_l)