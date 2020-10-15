num=int( input( "Enter the n of the Armstrong Numbers that will be listed: " ) )
arms=[]
i=1
while len(arms)<num:
    digits = len (str(i))
    sumOfDigitsCube = 0
    for dgt in str(i):
        sumOfDigitsCube += int(dgt)**digits
    if sumOfDigitsCube == i :
        arms.append(i)
    i += 1
print( arms )
#7 sn

