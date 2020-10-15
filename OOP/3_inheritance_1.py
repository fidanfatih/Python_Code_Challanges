class Animal(object):
    def __init__(self):
        print("animal")

    def walk( self ):
        print("animal walks")

class Monkey(Animal):
    def __init__(self):
        super().__init__()

    def climb( self ):
        print("animal climps")

class Bird(Animal):
    def __init__(self):
        super().__init__()

    def fly( self ):
        print("birds fly")

m1=Animal()
m1.walk()
print("-------------")
m2=Monkey()
m2.walk()
m2.climb()
print("-------------")
m3=Bird()
m3.walk()
m3.fly()
print("-------------")