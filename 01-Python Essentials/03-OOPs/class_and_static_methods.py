class Player:
    # Class object attribute
    membership = True
    def __init__(self, name = 'anonymous', age = 0):
        if Player.membership:
            self.name = name # attribute
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")

    @classmethod
    # cls -> Class
    def adding_num(cls, n1,n2):
        return cls('Teddy', n1 + n2)
    
    @staticmethod
    def adding_num(n1,n2):
        return n1 + n2

    

p1 = Player('Tom', 20)
print(p1.adding_num(2,3))

p3 = Player.adding_num(8,3)
print(p3.age)