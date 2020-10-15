numberOfList=int(input("Enter the n of Tribonacci Numbers: "))
n=[0,0,1]
if numberOfList<3:
    print(*n[:numberOfList])
else:
    for i in range (3,numberOfList):
        n.append(n[i-1]+n[i-2]+n[i-3])
print(*n)

# Alternatif çözüm
t=[0,0]
a, b, c = 1, 0, 0
for _ in range ( numberOfList-2 ):
    a , b , c = b , c , a + b + c
    t.append(c)
print(*t)