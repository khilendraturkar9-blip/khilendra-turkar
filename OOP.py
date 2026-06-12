# Q1 Create a class Employee with:

class Employee:
    #  Private variable
    __salary = 50000
    
    # Method increment()
    def increment (self):
        self.__salary +=10000
    #  Method deduct()
    def deduct(self):
        self.__salary -= 5000
    # Method get_salary()
    def get_salary (self):
        print("Salary:", self.__salary)
#Create 2 objects and call all methods on both
emp1 = Employee()
emp2 = Employee()
emp1.get_salary()
emp1.increment()
emp1.deduct()

emp2.increment()
emp2.deduct()
emp2.get_salary()


# Q2. Create Abstract class Vehicle with
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

# Child class Car
class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def fuel_type(self):
        print("Car uses petrol")


# Child class Bike
class Bike(Vehicle):

    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")

    def fuel_type(self):
        print("Bike uses petrol")

# Child class Tesla

class Tesla(Vehicle):

    def start(self):
        print("Tesla started")

    def stop(self):
        print("Tesla stopped")

    def fuel_type(self):
        print("Electric")

# Create objects
car = Car()
bike = Bike()
tesla = Tesla()

# Call methods
car.start()
car.stop()
car.fuel_type()

print()

bike.start()
bike.stop()
bike.fuel_type()

print()
tesla.start()
tesla.stop()
tesla.fuel_type()


# Q3. Create a Hybrid Inheritance program:
# Parent class
class Father:
    def property(self):
        print("Father's property")

    def business(self):
        print("Father's business")

# Child class 
class Son(Father):
    def study(self):
        print("son is studying ")

# Child class
class Daughter(Father):
    def dance(self):
        print("daughter is dancing")

class GrandChild(Son, Daughter):
    def gaming(self):
        print("grandchild is gaming")

# Create object
gc = GrandChild()

# Call all methods
gc.property()
gc.business()
gc.study()
gc.dance()
gc.gaming()