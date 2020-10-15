# https://www.hackerrank.com/challenges/designer-door-mat/problem

# row, col = map(int,input().split())
# for i in range(1,row,2):
#     print((i * ".|.").center(col, "-"))
#
# print("WELCOME".middle(col,"-"))
# for i in range(row-2,-1,-2):
#     print((i * ".|.").center(col, "-"))

row, col= map(int,input().split())
up=[ (row // 2 - i) * 3 * "-" + (2 * i + 1) * ".|." + (row // 2 - i) * 3 * "-" for i in range( row // 2 ) ]
middle=[ (col - 7) // 2 * "-" + "WELCOME" + (col - 7) // 2 * "-" ]
print( *(up + middle + up[ ::-1 ]) , sep="\n" )