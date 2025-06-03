from abc import ABC, abstractmethod
class Animal:
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can slither")
class Dog(Animal):
    def move(self):
        print("I can walk and run")
class Lion(Animal):
    def move(self):
        print("I can walk and run")
R = Human()
R.move()
K = Snake()
K.move()
L = Dog()
L.move()
M = Lion()
M.move()