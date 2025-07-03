class Player:
    # Class object attribute
    membership = True
    def __init__(self, name = 'anonymous', age = 0):
        if Player.membership:
            self.name = name # attribute
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")

p1 = Player('Tom', 455)
p2 = Player('henry', 344)
p3 = Player()
print(p1.membership)
print(p2.membership)
print(p1.age)

p1.shout()
p3.shout()