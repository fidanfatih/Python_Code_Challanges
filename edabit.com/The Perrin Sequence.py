# https://edabit.com/challenge/MfypAQedEAun4oQFA
def perrin(n):
    p = [ 3 , 0 , 2 ]
    for i in range(3,n+1):
        p.append(p[i-3]+p[i-2])
    return p[n]

# alternatif
# perrin=lambda n:[3,0,2][n]if n<3 else perrin(n-2)+perrin(n-3)

print(perrin (58))