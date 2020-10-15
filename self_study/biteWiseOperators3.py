# girilen stringte karakterlerde 1 leri yerine *, 0 ları yerine - koyan
#tüm stringi binariye çeviren program

import math
string=input("Enter a string: ")
number=0
# print(bitlenght,"bits : ",ord(string),end="")

for index in range(0,len(string)):
    number+=ord(string[index])*int(math.pow(2,8*index))  #ord, karakterin ASCII kodunu int tipinde döndürür
print(f"ASCII Code of {'string'} = {number}")
print(f"{len(bin(number))-2} bits : {bin(number)[2:]}")
bitlenght=int(math.log(number,2))+1
print(bitlenght,"bits : ",end="")
for bitNo in range (bitlenght-1,-1,-1):
    shiftedNumber = number>>bitNo
    bitValue = shiftedNumber & 1      #shiftedNumber ın son biti ile 1 and yapılır.
    if bitValue ==1:
        print("*",end="")
    else:
        print("-",end="")

