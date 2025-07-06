class User:
    def sign_in(self):
        print('Logged in')
    
# Extending the User functionality to Wizard and Archer class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')



class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with {self.num_arrows}')




wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 500)

wizard1.sign_in()
archer1.sign_in()

wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, Archer))
