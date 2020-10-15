# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
from functools import reduce
from time import time
t1=time()
def maximumToys(prices, k):
    prices.sort()
    for i in range(len(prices)-1,-1,-1):
        if reduce(lambda a,b:a+b,prices[:i])<=k:
        # if sum(prices[:i])<=k:
            print(len(prices[:i]))
            break

n,k=map(int,input().split())
prices=list(map(int,input().split()))
maximumToys(prices,k)
print(time()-t1)