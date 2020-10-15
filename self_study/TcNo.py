def isValid(tcNo:str) ->bool:
    try:
        int(tcNo)
    except ValueError:
        print("Tc Number must have only digits!")
        return False

    if(len(tcNo)!=11):
        print("Tc Number must have 11 digits!")
        return False

    addOddIndis=0
    addEvenIndis=0
    addIndis=0
    for i in range(0,9,2):
        addOddIndis+=int(tcNo[i])
    for i in range(1,9,2):
        addEvenIndis+=int(tcNo[i])
    if (7*addOddIndis-addEvenIndis)%10 == int(tcNo[9]):
        for i in range(0,10):
            addIndis+=int(tcNo[i])
        if(addIndis%10==int(tcNo[10])):
            return True
    return False


tcNo=input("Enter Your Tc Identity Number: ")
if(isValid(tcNo)):
    print("Tc Number is VALID...")
else:
    print("Tc Number is INVALID...")

