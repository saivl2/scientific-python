for item in [11,2,3]:
    print(item)
    print(item + 1)
print(item)

print()
for x in (1,2,3):
    for y in ['a', 'b', 'c', 'd']:
        print(x, y)

# Iterable -> List, dict, tuple, set, set

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)
