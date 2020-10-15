# https://edabit.com/challenge/XQwPPHE6ZSu4Er9ht
def is_economical ( n ) :
    prm , pow = [ ] , [ ]
    prm = prime_fact(n)
    pow = power(prm ,pow, n).copy()
    return "Equidigital"*(sum([len(str(i)) for i in pow+prm if i!=1])==len(str(n)))\
           or"Wasteful"*(sum([len(str(i)) for i in pow+prm if i!=1]) > len(str(n)))\
           or"Frugal"

def prime_fact(n):
    return [i for i in get_primes(n) if not n%i]

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers-=set(range(p * 2 , n + 1 , p))
    return primes

def power(prm,pow,num):
    count=0
    for i in prm :
        while (not num % i) :
            num /= i
            count += 1
        pow.append(count)
        count = 0
    return pow


print(is_economical(1522000))