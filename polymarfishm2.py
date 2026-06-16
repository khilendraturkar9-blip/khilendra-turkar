class Father :
    def marriage(self):
        print("Marry to anisha")

class Son(Father):
    def marriage(self):
        print("marry to mithali")

s = Son()
s.marriage()