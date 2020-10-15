def pascal(row):
    newList=list()
    numbers=[[1],[1,1]]
    for i in range(2,row):
        newList.append (1)
        for j in range(i-1):
            newList.append (numbers[i-1][j]+numbers[i-1][j+1])
        newList.append(1)
        numbers.append(newList)
        # print(numbers)
        newList=[]

    # print(numbers)
    for index,number in enumerate(numbers):
        print('  '*len(numbers[row-index-1])+("{:^5}"*len(number)).format(*number))

pascal(9)