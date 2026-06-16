class Grandfather:
    def __init__(self,name):
        self.name = name
    
    def prperty (self):
        print(f"(self.name)owns a house")
# parents
class Father (Grandfather):

    def bussiness(self):
        print(f"(self.name)runs a shop")
# child
class Sun(Father):
    def study(self):
        print(f"(self.name)is studyting")

# object
s = Sun("Rahul")
s.prperty()#Grandfather se mila
s.bussiness()#father
s.study()#sun
        


