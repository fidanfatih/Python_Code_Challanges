""""
Artık yıl 4ün katı olomalı.
100ün katı olan yıl, 400ün de katı ise artık yıldır.
örneğin 1900 artık yıl değil, 2000 artık yıldır.
"""
print("Leap Years between 1900-2020: ")
for i in range(1900,2021):
    if i%100==0 and i%400==0:
        print(i)
        continue
    if i%4==0 and i%100!=0:
        print(i)
