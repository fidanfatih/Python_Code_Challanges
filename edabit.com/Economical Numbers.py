# https://edabit.com/challenge/XQwPPHE6ZSu4Er9ht
def is_economical ( n ) :
    prm , pow = [ ] , [ ]
    prm = prime_fact(n)
    pow = power(prm ,pow, n)
    if sum([len(str(i)) for i in pow+prm if i!=1])==len(str(n)):
        return "Equidigital"
    elif sum([len(str(i)) for i in pow+prm if i!=1])>len(str(n)):
        return "Wasteful"
    else:
        return "Frugal"

def is_prime(n):
    return all([n%i for i in range(2,n)]) and n!=1

def prime_fact(n):
    return [i for i in range(2,n+1) if is_prime(i) and not n%i ]

def power(prm,pow,num):
    count=0
    for i in prm :
        while (num % i==0) : num /= i; count += 1
        pow.append(count)
        count = 0
    return pow


print(is_economical(81))