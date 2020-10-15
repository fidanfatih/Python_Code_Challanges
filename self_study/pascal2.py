def pascal(row):
    for index,number in enumerate(range(row)):
        print('  '*len(row_create(row-index-1))+("{:^5}"*len(row_create(index))).format(*row_create(index)))

def row_create(level):
    row=[1]
    for _ in range (level):
        row=[i+j for i,j in zip([0]+row,row+[0])]
    return row

pascal(9)