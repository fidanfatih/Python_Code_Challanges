from functools import reduce
def ekok(n1,n2):
    for i in range (n2,n1*n2+1):
        if not(i%n2 or i%n1): return i

def smallest(n):
    return reduce(lambda x,y:ekok(x,y),range(1,n))

print(smallest(15))