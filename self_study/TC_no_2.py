def isValid( tc:str ) ->bool:
    if not tc.isdecimal(): print("Tc No must have only digits!");return 0
    if len(tc)!=11: print("Tc No must have 11 digits!");return 0
    tc=[int(i) for i in tc]
    odd=sum([tc[i] for i in range(0,9,2)])
    even=sum([tc[i] for i in range(1,9,2)])
    if (7*odd-even)%10==tc[9]: return sum(tc[:10])%10==tc[10]

tc=input("Enter Your Tc Identity Number: ")
print(isValid(tc)*"Tc No is VALID..." or "Tc No is INVALID...")



#
# TCkimlik=11111111110
# mylist=[int(i) for i in str(TCkimlik)]
# def tckimlik(n):
#     sum1=(mylist[0]+mylist[2]+mylist[4]+mylist[6]+mylist[8])*7
#     mult=mylist[1]+mylist[3]+mylist[5]+mylist[7]
#     result1=sum1-mult
#     if result1%10!=mylist[9] and sum(mylist[:10])%10!=mylist[10]:
#         print('TC kimlik numarası geçersizdir')
#     else:
#         print('TC kimlik numarası geçerlidir')
# tckimlik(TCkimlik)