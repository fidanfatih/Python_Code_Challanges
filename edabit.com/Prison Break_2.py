# https://edabit.com/challenge/SHdu4GwBQehhDm4xT
A=[0, 0, 1, 1, 1, 0, 1]
count = 0
if A[0]==0: print(0)
else:
    k=1
    for i in A:
        if i==k:
            count+=1
            k=1-k
print(count)