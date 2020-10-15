def prime_factors(num):
    primes=[]
    for i in range(2,num+1):
        while not num%i:primes.append(i);num//=i
    return primes

print(prime_factors(200))