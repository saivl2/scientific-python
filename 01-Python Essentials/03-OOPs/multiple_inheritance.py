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
        print(f'Attacking with {self.num_arrows} arrows') # Added ' arrows' for clarity

    def run(self):
        print('Ran really fast')

class HybbridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        # Call the constructor of Wizard with 'name' and 'power'
        Wizard.__init__(self, name, power)
        # Call the constructor of Archer with 'name' and 'arrows'
        Archer.__init__(self, name, arrows)

h1 = HybbridBorg('Bobby', 3, 10)
h1.run()
h1.attack()