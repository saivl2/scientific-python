li = [1,2,3,4,5,6]
def check_odd(n):
    return n % 2 != 0


print(list(filter(check_odd, li)))