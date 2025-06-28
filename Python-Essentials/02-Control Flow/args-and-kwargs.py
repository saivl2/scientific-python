def super_func(*args, **kwargs):
    print(args) # Tuple
    print(kwargs)
    return sum(args) + sum(kwargs.values())

print(super_func(1,2,4))
print(super_func(1,2,3, n1=56, n2 = -900))

# Order: params, *args, default parameters, **kwargs