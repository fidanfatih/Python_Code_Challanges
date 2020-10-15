number=input("Enter a n(1-3999): ")
if int(number)<1 or int(number)>3999:
    print("Wrong entry...")
    exit(0)
romanValue=""
digitOfNumber=list(number)
for i in range(4-len(digitOfNumber)):
    digitOfNumber.insert(0,0)
romanList=['','I','II','III','IV','V','VI','VII','VIII','IX']\
          +['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']\
          +['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']\
          +['','M','MM','MMM']
for index,digit in enumerate(digitOfNumber):
    if index==0:
        romanValue+=romanList[int(digit)+30]
    elif index==1:
        romanValue+=romanList[int(digit)+20]
    elif index==2:
        romanValue+=romanList[int(digit)+10]
    elif index==3:
        romanValue+=romanList[int(digit)]
print(romanValue)