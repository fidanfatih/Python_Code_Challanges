# def name_shuffle(txt):
#     word=txt.split()
#     return word[-1],
#
#
# print(name_shuffle())

# txt="A B C"
txt= input("Ad Soyad Giriniz : ")
print(' '.join([txt.split()[-1]]+txt.split()[:-1]))
print(*txt.split()[-1:],*txt.split()[:-1])
print(txt.split()[-1],*txt.split()[:-1])
print(txt.split()[-1]+' '+txt[:txt.rfind(" ")])
print(txt[txt.rfind(" ")+1:]+' '+txt[:txt.rfind(" ")])
# a =input("İsim ve soyisim giriniz\n1")
# b =a.split()  #1
# b.insert(0, b[-1]) #2
# b.pop() #3
# print(" ".join(b))




