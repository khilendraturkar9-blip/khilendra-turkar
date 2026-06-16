# parent class
class Animal :
    def __init__(self,name):
        self.name = name
        

    def eat (self):
        print(f"{self.name} is eating")

# child class   
class Dog(Animal):
    def bark (self):
        print(f"{self.name} says woof")

# Object 
d = Dog("abhi")
d.eat()
d.bark()
