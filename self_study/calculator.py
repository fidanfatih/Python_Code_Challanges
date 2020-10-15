while True:
    operationData=input("Operator:{ + - * / % // ^}\nPress 'Q' to exit\n"
                        "Enter the operation string (number1 operator number2): ")
    operate=""
    if operationData.lower()=='q':
        print("Program is ended...")
        exit(0)
    if operationData.count(" ")!=2:
        print("Enter a space between items...\n")
        continue
    operationItems=operationData.split()
    try:
        operate = operationItems[1]
        number1=float(operationItems[0])
        number2=float(operationItems[2])
    except Exception:
        print("Please enter numeric values...\n")
        continue
    finally:
        if operate not in ['+', '-', '*', '/', '%', '//', '**']:
            print("Please enter a operator...\n")
            continue
    if operate=="+":
        result=number1+number2
    elif operate=="-":
        result=number1-number2
    elif operate=="*":
        result=result=number1*number2
    elif operate=="/" and number2 != 0:
        result=result=number1/number2
    elif operate=="%":
        result=result=number1%number2
    elif operate=="//" and number2 != 0:
        result=result=number1//number2
    elif operate=="**":
        result=result=number1**number2
    else:
        print("Dividind number can not be O...\n")
        continue

    print(f"{number1} {operate} {number2} = {result}\n")

