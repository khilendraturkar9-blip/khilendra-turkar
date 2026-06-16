class Parent:
    def property(self):
        print("father owns a house")
    def money(self):
        print("father has money" )
# child1
class Sun(Parent):
        def cricket(self):
            print("sun plays cricket")
# child2
class Doughter(parent):
        def dance(self):
            print("Doughter loves danc")

# child 3
class Youngersone(Parent):
    def gaming(self):
        print("youger one loves gaming")

# Objects
s= Sun()
s.property()
s.cricket()

d = Doughter()
d.property()
d.dance()

y = Youngersone()
y.property()
y.gaming()
