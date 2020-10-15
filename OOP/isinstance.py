class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Terrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

dog1 = Terrier("Miles", 4)
dog2 = Dachshund("Buddy", 9)
dog3 = Bulldog("Jack", 3)
dog4 = Bulldog("Jim", 5)

print(isinstance(dog4, Dog))
print(isinstance(dog1, Bulldog))
print(isinstance(dog1, Terrier))