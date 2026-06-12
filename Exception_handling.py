# # Q4. Create class AgeVerification:

# # Custom exceptions
# class UnderAgeError(Exception):
#     pass

# class InvalidAgeError(Exception):
#     pass

# class AgeVerification:
#     def set_age(self,age):
#         self.age = age

#         if age < 0:
#             raise ValueError("Age cannot be negative")
        
#         elif age < 18:
#             raise UnderAgeError("You are not 18 years old")
        
#         elif age > 120:
#             raise  InvalidAgeError("Age cannot be greater than 120")
        
#         else:
#             print(" Valid age !")

# # Create object
# p = AgeVerification()

# # Test cases
# p.set_age(15)
# p.set_age(100)

# Q5. Create a Login System:

class AccountLockedError(Exception):
    pass

class LoginSystem:
    __password = "python@123"
    __attempts = 3
    def login(self, password):
        try:
            if self.__attempts == 0:
                raise AccountLockedError("Account is locked!")

            elif  password == self.__password:
                print("Login successful!")

            else:
                self.__attempts -= 1
                print(f"Incorrect password! Attempts left: {self.__attempts}")

        except AccountLockedError as e:
            print(e)

        finally:
            print("Login attempt completed.")

# Create object
log = LoginSystem()
log.login("hfsifh")
log.login("abcd")
log.login("xyz")
log.login("test")