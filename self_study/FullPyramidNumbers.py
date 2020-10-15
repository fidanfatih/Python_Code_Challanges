row = 5
numbers =list()
first = middle = 1
for i in range ( row ):
    numbers.append ( list ( range ( first, middle + 1 )) + list ( range ( middle-1, first-1,-1) )  )
    first += 1
    middle += 2
for index,rowList in enumerate(numbers):
    print(' '*len(numbers[-(index+1)]),*rowList)
