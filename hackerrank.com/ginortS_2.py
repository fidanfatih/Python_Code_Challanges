# print("Sorting1234")
# print(*sorted("Sorting1234"),sep="")
# print(*(sorted("Sorting1234", key=lambda x: (x.islower(), x))), sep='')
# print(*(sorted("Sorting1234", key=lambda x: (x.isupper(),x.islower(), x))), sep='')
# print(*(sorted("Sorting1234", key=lambda x: (x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')

# f=map(lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x),"Sorting1234")
# for i in list(f):
#     print(i)


print(*(sorted("Sorting1234", key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))),sep='')

