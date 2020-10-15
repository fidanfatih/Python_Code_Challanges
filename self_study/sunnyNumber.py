# A n N is a sunny n if N + 1 is a perfect square.
from math import sqrt
num=int(input("is it a sunny n or not?\nEnter a n: "))
print(str(sqrt(num+1))[-2:]==".0")
