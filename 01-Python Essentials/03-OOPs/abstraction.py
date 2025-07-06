class Player:
    # Constructor
    def __init__(self, name, age):
        self.name = name # attribute
        self.age = age

    def run(self): # Method
        print('RUN')

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


p1 = Player('andrei', 100)
p1.speak() # Abstraction, you don't see what's inside speak()

print((1,2,3,3).count(3)) # We don't know how count() is implemented 


# Overwriting the attriutes of a class --> Concerning 
p1.name = '!!!'
print(p1.name)
p1.speak()
