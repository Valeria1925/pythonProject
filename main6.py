class Animal:
    def voice(self):
        pass

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
s.voice()

