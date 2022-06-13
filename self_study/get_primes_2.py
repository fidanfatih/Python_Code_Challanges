def is_prime(n):
    return n==2 or all([n%i for i in range(2,int(n**0.5)+1)]) and n not in [0,1]

def get_primes(n):
    primes = [i for i in range(2,n+1) if is_prime(i)]
    return primes
  
print(get_primes(250))