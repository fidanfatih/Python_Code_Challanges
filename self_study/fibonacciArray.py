def searchFibonacciNumber(lenghtOfList: int):
    fibonacciArray = [ 1, 1 ]
    if lenghtOfList == 1:
        return fibonacciArray[:1]
    elif lenghtOfList >= 2:
        for i in range ( 2, lenghtOfList ):
            fibonacciArray.append ( fibonacciArray [ -2 ] + fibonacciArray [ -1 ] )
        return fibonacciArray
    else:
        print ( "Hatalı değer girdiniz..." )


lenghtOfList = int ( input ( "Enter the lenght of the fibonacci array to be listed: " ) )
fibonacciNumbers = searchFibonacciNumber ( lenghtOfList )
print ( *fibonacciNumbers )

# Alternatif çözüm
fibonacciArray=[ 1, 1 ]
a, b = 1, 1
for i in range ( lenghtOfList-2 ):
    a , b = b , a + b
    fibonacciArray.append( b )
print( *fibonacciArray[ :lenghtOfList ] )
