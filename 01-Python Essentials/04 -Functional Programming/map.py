def multiply_by2(item):
    return item * 2


# map(function, seq)

result = list(map(multiply_by2, [1,2,3,4]))
print(result)

print(list(map(multiply_by2, (1,2,3,4))))
