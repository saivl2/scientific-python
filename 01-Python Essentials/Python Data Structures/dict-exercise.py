# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user = {
    'username': 'kyle34', 
    'age': 25,
    'weapons': ['keyblade', 'BFG'],
    'is_active': False,
    'clan': 'savage' 
}

# 2 iterate and print all the keys in the above user.
print(user.keys())

# 3 Add a new weapon to your user
user['weapons'].append('Shotgun')
print(user)

# 4 Add a new key to include 'is_banned'. Set it to false
user['is_banned'] = False
print(user)
# 5 Ban the user by setting the previous key to True
user['is_banned'] = True
print(user)
print()
# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user.copy()
user2['username'] = 'jamey6'
user2['age'] = 45
print(user)
print()
print(user2)