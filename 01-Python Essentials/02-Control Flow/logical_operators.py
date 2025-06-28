print(4 > 5)
print(4 < 5)
print(5 == 5.0)
print(9.3 >= 9.31)
print(2 <= 2.0)

print('a' > 'b')
print('a' > 'A')
print(1 != 2)
print()
print(not True)
print(not(1 == 1))
print('-'* 23)

is_magician = False
is_expert = True

if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_magician:
    print('at least you\'re getting there')
elif not is_magician:
    print('You need magic powers')