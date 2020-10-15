# https://edabit.com/challenge/5ou6SKDtFRZugbpda
def additive_persistence ( n ) :
    count=0
    while n//10:
        n=sum([int(i) for i in str(n)])
        count+=1
    return count

def multiplicative_persistence ( n ) :
    count,multiple = 0,1
    while n // 10 :
        for i in str (n): multiple*=int(i)
        count += 1
        n=multiple
        multiple=1
    return count

print(additive_persistence(19999999999999999999999))
print(multiplicative_persistence(277777788888899))