def is_economical ( n ) :
    x , y = [ ] , len(str(n))
    for i in range(2 , n + 1) :
        while n % i == 0 :
            x += [ i ]
            n /= i
    x = sum(len(str(i)) + (x.count(i) and x.count(i) > 1) for i in set(x))
    return "Frugal" if x < y else "Wasteful" if x > y else "Equidigital"


print(is_economical(1500002))
