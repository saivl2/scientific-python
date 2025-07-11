# 1. Given the same input, it will return the same output always.
# 2. A function should not produce any side effects. (Effects the output)

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

l = [1,2,3]

print(multiply_by2(l))