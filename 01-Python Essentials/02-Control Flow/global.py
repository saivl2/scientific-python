total = 0

def count(total):
    # global total
    total += 1
    return total

print(count(total)) # 1
# print(count())
# print(count())
print(count(count(total)))