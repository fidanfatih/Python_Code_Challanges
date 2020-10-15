# Roots of the 2nd degree equation
import math
a=float(input("Enter the coefficients of the 2nd degree equation\na:"))
b=float(input("b:"))
c=float(input("c:"))
delta=b*b-4*a*c
if (delta<0):
    print("There is no root!")
elif(delta==0):
    print(f"Root is {-b/(2*a)}")
else:
    print(f"1st root is {(-b-math.sqrt(delta))/(2*a)}\n2st root is {(-b+math.sqrt(delta))/(2*a)})")

i=input("")