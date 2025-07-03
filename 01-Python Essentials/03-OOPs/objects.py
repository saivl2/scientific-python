# OOP - A way to think about our code and structure our code.
class Player:
    # Constructor
    def __init__(self, name, age):
        self.name = name # attribute
        self.age = age

    def run(self): # Method
        print('RUN')
    

player1 = Player("Cindy", 23)
player2 = Player('Tom', 34)
print(player1.name)
print(player1)
print()
print(player2.name)
print(player2.age)
player1.run()
player2.attack = 50
print(player2.attack)
print()
help(player1)
help(set)