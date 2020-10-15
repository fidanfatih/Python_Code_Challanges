# https://www.hackerrank.com/challenges/greedy-florist/problem
def getMinimumCost(k,c):
    c=sorted(c)[:n]
    f,t,x=[],len(c),1
    for i in range(t//k+1):
        for j in range(1,(k+1)*(t>=k) or len(c)%k+1):
            f.append(c[:t][-j]*x)
        t,x=t-k,x+1
    return sum(f)

n,k=map(int,input().split())
prices=list(map(int,input().split()))
print(getMinimumCost(k,prices))

"""
5 3
1 3 5 7 9
29

3 3
2 5 6
13
"""