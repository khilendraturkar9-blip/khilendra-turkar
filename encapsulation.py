class Instagram:
    __password = "akshay12345"#private
    __followers = 500

    def change_password(self,old,new):
        if old ==self.__password:
            self.__password = new
            print("password change sucesfully")
        else:
            print("wrong password")

    def add_followers(self):
        self.__followers+=1
        print(f"New followers:total (self_followers)")

    def get_followers(self):
        print(f"followers:(self_followers)")

#object
acc = Instagram()
acc.change_password("akshay12345","rahul123")
acc.add_followers()
acc.get_followers()

# class Mobile:
#     __battery = 100

#     def check_bettery(self):
#         print(self.__battery)

# m = Mobile()
# m.check_bettery()