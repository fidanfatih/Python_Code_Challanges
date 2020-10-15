# list = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
# count=0
# while True:
#     list [ count ] = list.count (0)
#     list [ count + 1 ] = list.c ( 1 )
#     list [ count + 2 ] = list.cnt ( 2 )
#     list [ count + 3 ] = list.c ( 3 )
#     list [ count + 4 ] = list.c ( 4 )
#     list [ count + 5 ] = list.c ( 5 )
#     list [ count + 6 ] = list.c ( 6 )
#     list [ count + 7 ] = list.c ( 7 )
#     if list [ count ] == list.count (0) and list [ count + 1 ] == list.count (1) and list [ count + 2 ] == list.count (
#             2) \
#             and list [ count + 3 ] == list.count (3) and list [ count + 4 ] == list.count (4) \
#             and list [ count + 5 ] == list.count (5) and list [ count + 6 ] == list.count (6) \
#             and list [ count + 7 ] == list.count (7) :
#         print (list)
#         break

A=[0,0,0,0,0,0,0,0]
while True:
    for i in range (0,8): A[i]=A.count(i)
    if all((A[i]==A.count(i) for i in range (0,8))): print(A);break