# https://www.hackerrank.com/challenges/nested-list/submissions/code/171623545
def seach(A):
    A=sorted(A,key=lambda x:x[1])
    t=len([i for i in A[1:] if A[0][1]==i[1]])+1
    B=sorted([A[t]]+[i for i in A[1+t:] if A[t][1]==i[1]],key=lambda x:x[0])
    return [i[0] for i in B]

n,A=int(input()),[]
if 2<=n<=5:
    for i in range(n):
        A.append([float(input()) if i else input() for i in range(2)])
    print(*seach(A),sep="\n")

"""
1
Harry
37.21
Berry
37.21
Tina
37.2
Harry
37.21
Harsh
37.21
"""