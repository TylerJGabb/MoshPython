class Animal:
    def __init__(self):
        print('Animal constructor')
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def __init__(self):
        print('Mammal constructor')
        self.weight = 2
        super().__init__()
        #  without a call to super, the __init__ method is overwritten and we loose the superclass initializer

    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()
print(m.age)
print(m.weight)