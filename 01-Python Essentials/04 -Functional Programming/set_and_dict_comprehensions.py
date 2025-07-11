s = {n ** 2 for n in range(1,100)}
print(s)
print()

d0 = {
    'a': 1, 
    'b': 4
}

d = {
    k: v ** 2 for k, v in d0.items() if v % 2 == 0
}

print(d)