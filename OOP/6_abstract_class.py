from abc import ABC,abstractmethod  #abc :abstract base class

class Animal(ABC): # super class
    @abstractmethod  # buna abstract method decorator denir.
    def walk( self ): pass

    @abstractmethod
    def run( self ): pass

class Bird(Animal): # sub class
    def __init__(self):
        print("bird")

    def walk( self ):
        print("walk")

    def run( self ):
        print("run")


"""
Python absract class için altyapı sağlamıyor, built in modül kullanarak bunu yaparız.
Animal classını ABC den inherit ederek ve abstract method decorator kullanarak abstrack class yaparız.
1-Abstrack class tan direkt olarak object türetilemez.
2-Abstract class ta kullanılan bir method muhakkak sub classta kullanılmak zorunda

"""
# a1=Animal() # yanlış kullanım
# Abstrack class tan direkt olarak object türetilemez.

b1=Bird()
b1.walk()
b1.run()

