user = {
    'name': 'bobby',
    'status': 'Single'
}


print(user.get('age', 0))

# Another way to create a dictionary
user2 = dict()

user2['name'] = 'Jamey'
user2['age'] = 34

print(user2)

print('bobby' in user2) # Default is the key
print(34 in user2.values())

print(user2.items())

print(user2.pop('age'))
print(user2)

user2.update({'is_cool': True})
print(user2)