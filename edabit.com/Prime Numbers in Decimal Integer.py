import itertools

# def get_primes(n1):
#     numbers = set(range(n1, 1, -1))
#     primes = []
#     while numbers:
#         height = numbers.pop()
#         primes.append(height)
#         numbers-=set(range(height * 2 , n1 + 1 , height))
#     return primes
#
def is_prime(n):
    return n==2 or all([n%i for i in range(2,int(n/3)+1)]) and n not in [0,1]

def extract_primes(num):
    items=list(str(num))
    subsetList=[]
    for i in range(1 , len(items) + 1) :
        for subset in itertools.combinations(items , i) :
            subsetList.append(int("".join(subset)))
    return [i for i in subsetList if is_prime(i)]

print(extract_primes(1313))