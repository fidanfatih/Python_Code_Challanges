# https://edabit.com/challenge/BfSj2nBc33aCQrbSg
def truncatable(n):
    left,right=left_split(n),right_split(n)
    return "0" not in str(n) and ("both"*left*right or "right"*right or "left"*left or False)

def left_split(n):
    return all([is_prime(int(str(n)[i:])) for i in range(len(str(n)))])

def right_split(n):
    return all([is_prime(int(str(n)[:i+1])) for i in range(len(str(n)))])

def is_prime(n):
    return n==2 or all([n%i for i in range(2,n//3+2)]) and n not in [0,1]

print(truncatable(47))