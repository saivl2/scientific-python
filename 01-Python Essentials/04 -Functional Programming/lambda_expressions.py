# lambda param: func(param)

mul = lambda n: n * 2

print(list(map(mul, [1,2,3])))
print(type(mul([1,2])))
print(type(mul))

print()

print(list(map(lambda n: n ** 2, [1,2,3])))

# List Sorting on 2nd  index

li = [(0, 2), (4, 3), (9, 9), (10, -1)]

# n = Tuple here
li.sort(key = lambda n: n[1])
print(li)
