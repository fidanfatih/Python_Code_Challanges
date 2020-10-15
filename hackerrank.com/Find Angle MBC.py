# https://www.hackerrank.com/challenges/find-angle/problem
from math import atan,degrees
ab,bc=[int(input()) for _ in range(2)]
print((lambda x,y:round(degrees(atan(x/y))))(ab,bc),'°',sep='')