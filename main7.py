class Animal:
    counter = 0

    def __init__(self):
        Animal.counter =3
    def voice(self):
        pass
    @staticmethod
    def getCounter():
        return Animal.counter


class Cat(Animal):
    def voice(self):
       print('myau')

s=Cat()
s.voice()

class Dog(Animal):
    def voice(self):
       print('arrr')

s=Dog()
s.voice()

class Duck(Animal):
    def voice(self):
       print('kryaa')

s=Duck()
s=Duck()
s.voice()

print(Animal.getCounter())