class User:
    def __init__(self, email):  # Corrected __init__
        self.email = email

    def sign_in(self):
        print('Logged in')

# Extending the User functionality to Wizard and Archer class
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):  # Added email parameter
        super().__init__(email)  # Call to parent constructor
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with {self.num_arrows} arrows')


w1 = Wizard('Merlin', 34, 'merlin@yahoo.com')
print(w1.email)  # Corrected to access email as an attribute

print(dir(w1))

a1 = Archer('Robin', 100, 'robin@gmail.com') # Example of creating an Archer instance
print(a1.email)
a1.attack()