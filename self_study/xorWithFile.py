# dosyadan verileriçek, her baytı 15 ile Xorla, başka dosyaya yazdır.

fileName="deneme2.txt"
with open(fileName, "rb") as fileObject :  # mevcut dosyayı okumak için "r" kullanırız.
    fileContent= fileObject.read()  # open içinde ne yapılacağı yazılmamışsa default olarak "r" kabul edilir.
    newFileContent=""
    for byte in fileContent:
        newFileContent +=chr(byte ^ 15)

with open(f"{fileName}.new", "w") as fileObject :
    fileObject.write(newFileContent)
