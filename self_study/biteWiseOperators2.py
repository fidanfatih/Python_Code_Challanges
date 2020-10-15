# girilen sayının 1leri yerine *, 0ları yerine - koyan program
import math
number=int(input("Enter a number: "))
print(f"{len(bin(number))-2} bits : {bin(number)[2:]}")
print(f"{len(bin(number))-2} bits : {bin(number)[2:].replace('0','-').replace('1','*')}\n")

# alternatif yöntem
bitlenght=int(math.log(number,2))+1
print(bitlenght,"bits : ",end="")
for bitNo in range (bitlenght-1,-1,-1):
    shiftedNumber = number>>bitNo
    bitValue = shiftedNumber & 1      #shiftedNumber ın son biti ile 1 and yapılır.
    if bitValue ==1:
        print("*",end="")
    else:
        print("-",end="")

