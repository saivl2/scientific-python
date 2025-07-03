#Given the below class:
class Cat:
    species = 'mammal' # Class Object attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
c1 = Cat('Jinny', 3)
c2 = Cat('Dank', 4)
c3 = Cat('Frank', 5)

cat_ages = [c1.age, c2.age, c3.age]

# 2 Create a function that finds the oldest cat

def oldest_cat(cat):
    return max(cat_ages)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {oldest_cat(cat_ages)} years old.")