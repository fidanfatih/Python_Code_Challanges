class Employee:
    def raisee( self ):
        raise_rate=0.1
        return 100+100*raise_rate

class Ce(Employee):
    def raisee( self ):
        raise_rate=0.2
        return 100+100*raise_rate

class Eee(Employee):
    def raisee( self ):
        raise_rate=0.3
        return 100+100*raise_rate

# Aynı fonksiyon farklı değer döndürüyor. Aynı zamanda overriding.

e1=Employee()
print(e1.raisee())

ce=Ce()
ee=Eee()

employees=[ce,ee]
for employee in employees:
    print ( employee.raisee ( ) )