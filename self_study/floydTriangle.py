# row=5
# num=[]
# first=last=add=1
# for i in range(row):
#     num.append( list( range( first , last + 1 ) ) )
#     first=last+1
#     last=first+add
#     add+=1
# for rowList in num:
#     print( *rowList )

row=int(input('Enter row n:'))
num=list(range(1,row*(row+1)//2+1))
for i in range(1,row+1): print(*num[:i]);num=num[i:]




