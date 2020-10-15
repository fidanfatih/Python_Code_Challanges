def is_prime(n):
    return n==2 or all([n%i for i in range(2,int(n**0.5)+1)]) and n not in [0,1]

def prime_factors(num):
    primes_uniq,primes=[i for i in range(2,num+1) if not num%i and is_prime(i)],[]
    while num>1:
        for i in primes_uniq:
            if num%i==0:num//=i;primes.append(i);break
    return primes


print(prime_factors(200))