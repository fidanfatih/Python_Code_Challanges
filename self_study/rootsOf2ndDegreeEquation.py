print("Root(s) of a.X^2 + b.X + c = 0")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
delta=b*b-4*a*c
if delta==0:
    print(f"Root is {(-b-delta**0.5)/(2*a)}")
elif delta>0:
    print ( f"Roots are {(-b - delta ** 0.5) / (2 * a)} and {(-b+delta**0.5)/(2*a)}" )
else:
    print("It has no root")

