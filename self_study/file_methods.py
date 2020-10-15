poem=open("istiklal_marşı.txt","r",encoding="utf-8") # encoding utf-8 yazılmazsa türkçe kazakterler yazılmaz.
print(poem.readline())
print(poem.readlines()) # curser ın kaldığı yerden her satırı listenin elemanı yapar

my_file = open("fishes.txt","r")

print(type(my_file))
