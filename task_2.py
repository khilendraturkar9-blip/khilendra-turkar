# # polymorphism
# class Car:
#     def drive(self):
#         print(f"Car is driving")
#     def bike(self):
#         print(f"bike is driving")
#     def cycle(self):
#         print(f"cycle is dirving")

# c = Car()   
# c.drive()
# c.bike()
# c.cycle()

# # Encapsulation
# class MobilePhone:
#     __battery = 100

#     def charge(self):
#         self.__battery += 10
#         print(f"bettery charged: {self.__battery}%")
#     def use_phone(self):
#         self.__battery -=20


# task2
# num = int(input("enter a nambur:"))
# a  = num/100
# try:
#     num ==0
#     print("cannot divide by zero")
# except:
#     print("please enter a valid number")
# else:
#     print(f"result:{a}")

a = 10
b= 0
try:
    num = int(input("enter the nambur"))
    print(10/num)
except ZeroDivisionError:
    print("dont divide with zero")
except ValueError:
    print("type nambur only ")