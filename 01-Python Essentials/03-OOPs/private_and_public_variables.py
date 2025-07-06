class Player:
    # Constructor
    def __init__(self, name, age):
        # Private Variable
        self._name = name # attribute
        self.age = age # Public Variable

    def run(self): # Method
        print('RUN')

    def speak(self):
        print(f"My name is {self._name} and I am {self.age} years old.")


p1 = Player('andrei', 100)
p1.speak()
