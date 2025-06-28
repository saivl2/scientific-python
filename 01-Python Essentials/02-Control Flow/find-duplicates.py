some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
no_duplicates = []
duplicates = []
for item in some_list:
    if item not in no_duplicates:
        no_duplicates.append(item)
    else:
        duplicates.append(item)
print(duplicates)