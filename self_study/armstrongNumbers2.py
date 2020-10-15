def findNumberOfDigits(number:int) ->int:
    numberOfDigits = 1
    while number > 0:
        if number // 10 == 0:
            break
        else:
            number = number // 10
            numberOfDigits += 1
    return numberOfDigits


def findListOfDigits(number:int) ->list:
    listOfDigits=list()
    while number>0:
        listOfDigits.append(number%10)
        number=number//10
    return listOfDigits


numberOfList = int (input ("Enter the n of the Armstrong Numbers that will be listed: "))
armstrongNumbers = list ( )
number = 1
while len(armstrongNumbers)<numberOfList:
    numberOfDigits=findNumberOfDigits(number)
    listOfDigits=findListOfDigits(number)
    sumOfDigitsCube = sum(list ( map ( lambda x: x ** numberOfDigits, listOfDigits ) ))
    # sumOfDigitsCube=0
    # for digit in listOfDigits:
    #     sumOfDigitsCube+=digit**numberOfDigits
    if number==sumOfDigitsCube:
        armstrongNumbers.append(number)
    number+=1
print (armstrongNumbers)
#10 sn