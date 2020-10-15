# https://edabit.com/challenge/dSrisJKHB78aj2d7L
import time
def triangle(p,area):
    f=lambda a,b,c:(p*(p-2*a)*(p-2*b)*(p-2*c))**0.5/4
    result=[]
    for a in range(p//3,p):
        for c in range(p//3,0,-1):
            b=p-a-c
            if abs(f(a,b,c)-area)< 0.5 and sorted([a,b,c]) not in result:
                result.append(sorted([a,b,c]))
    return sorted(result)

t0=time.time()
print(triangle(864, 23760))
print(time.time()-t0)