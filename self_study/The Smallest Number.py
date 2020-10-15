
# def primes(n):
#     return [i for i in range(n) if is_prime(i)]
#
# def is_prime(n):
#     return n==2 or all([n%i for i in range(2,int(n**0.5)+1)]) and n not in [0,1]
#

# def prime_factors(num):
#     primes=[]
#     for i in range(2,num+1):
#         while not num%i:primes.append(i);num//=i
#     return primes
#
# print(prime_factors(150))

from functools import reduce

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers-=set(range(p * 2 , n + 1 , p))
    return primes

def ekok(n1,n2):
    for i in range (n2,n1*n2+1):
        if not(i%n2 or i%n1): return i

def smallest(n):
    a=set(range(1,n+1))-set(get_primes(n))
    b=reduce(lambda x,y:x*y,get_primes(n))
    return reduce(lambda x,y:ekok(x,y),[b]+list(a))

print(smallest(17))