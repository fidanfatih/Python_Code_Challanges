def is_prime(n):
    return n==2 or all([n%i for i in range(2,int(n**0.5)+1)]) and n not in [0,1]

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers-=set(range(p * 2 , n + 1 , p))
    return primes



list1=set(get_primes(1000))
list2=set(range(0,1001))
for i in list2-list1:
    print(is_prime(i))