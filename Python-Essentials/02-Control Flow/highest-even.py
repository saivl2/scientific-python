li = [1,2,3,4,8]

def is_even(n):
    return n % 2 == 0

def highest_even(li):
    evens = []
    for item in li:
        if is_even(item):
            evens.append(item)
    return max(evens)

print(highest_even(li))
    
