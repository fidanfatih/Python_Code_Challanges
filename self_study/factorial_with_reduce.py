from functools import reduce

def fact(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

print(fact(5))