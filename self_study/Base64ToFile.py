#bir dosyadan metin dosyasını alıp base64 çevirip başka dosyaya yazan program.

from base64Methods import stringToBase64

with open("sample.txt", "r", encoding="utf-8") as fileObject :  # mevcut dosyayı okumak için "r" kullanırız.
    text = fileObject.read()  # open içinde ne yapılacağı yazılmamışsa default olarak "r" kabul edilir.
    text=stringToBase64(text)
with open("deneme3.txt","w",encoding="utf-8") as fileObject:
    fileObject.write(text)