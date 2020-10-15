def list_str(n):
    return '   '.join([str(i) for i in n])

def row_create(level):
    row=[1]
    for _ in range (level):
        row=[i+j for i,j in zip([0]+row,row+[0])]
    return list_str(row)

def pascal(n):
    for i in range(0,n):
        print(row_create(i).center(5*n," "))

pascal(9)