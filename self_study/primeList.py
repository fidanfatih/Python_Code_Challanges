
def primes(n):
    primes,num = [ 2 ],3
    while len(primes)<n:
        for i in range(2,num):
            if num % i == 0:
                num += 1
                break
        else:
            primes.append(num)
            num+=2
    return primes


lenght=int( input( "How many prime numbers would you like to list? : " ) )
print(primes(lenght))