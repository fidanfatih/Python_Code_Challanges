A=[0]*8
# while True:
#     for i in range (0,8): 
#         A[i]=A.count(i)
#     if all([A[i]==A.count(i) for i in range (0,8)]):
#         print(A)
#         break

A=[0]*8
while True:
    for i in range (0,8): A[i]=A.count(i)
    if all((A[i]==A.count(i) for i in range (0,8))): print(A);break