#ismini kullanıcının girdiği dosyadaki karakter sayısı, satır sayısı, kelime sayısı, en uzun kelimenin uzunluğunu bulalım.

import os

while True:
    fileName = input("Enter the file name:(Çıkmak için ENTER'a basınız) ")
    if fileName =='':
        break
    if os.path.isfile(fileName)==False:      #os.path.isfile() dosya adı mevcutsa True döndürür.
        print("There is no file in this name... 😞😞😞\n")
        continue

        #os.path.isfile() alternatif olarak try-except ile de yapılabilir.
    """
    try:
        file= open(fileName,"r",encoding="utf-8")
    except FileNotFoundError:
        print("There is no file in this name... 😞😞😞\n")
        continue
    """

    punctuation=".,:;!'?%=()[]{}/\*+-"+'"'
    lineList = []
    lenghtOflenghtiestWord=0

    with open(fileName, "r", encoding="utf-8") as fileObject :
        for line in fileObject.readlines() :
            lineList.append(line)

        fileObject.seek(0)
        textString=str(fileObject.read())
        numberOfCharacter = len(textString)
        for sign in punctuation:
            for character in textString:
                if character==sign:
                    textString.replace(sign,"")

        for word in textString.split():
            if lenghtOflenghtiestWord<len(word):
                lenghtOflenghtiestWord=len(word)
                lenghtiestWord=word

    numberOfWords=len(textString.split())
    numberOfLines = len(lineList)
    print(f"Number of character  in the file: {numberOfCharacter}")
    print(f"Number of lines in the file: {numberOfLines}")
    print(f"Number of words in the file: {numberOfWords}")
    print(f"The lenghtiest word in the file: '{lenghtiestWord}'")
    print(f"Lenght of the lenghtiest word in the file: {lenghtOflenghtiestWord}\n")

print("Programdan kapanıyor... 👋👋👋")