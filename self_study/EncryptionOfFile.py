def encryptFile(fileNameParam:str, passwordParam:int) ->None:
    with open(fileNameParam, "r", encoding="utf-8") as fileObject:
        fileContent=fileObject.read()
    encryptedContent=""
    for character in fileContent:
        encryptedContent+=chr(ord(character)^passwordParam)

    with open(f"{fileNameParam}.enc","w", encoding="utf-8") as fileObject:
        fileObject.write(encryptedContent)


def decryptFile(fileNameParam: str, passwordParam: int) -> None:
    with open(fileNameParam, "r", encoding="utf-8") as fileObject:
        encryptedContent = fileObject.read()
    decryptedContent = ""
    for character in encryptedContent:
        decryptedContent += chr(ord(character) ^ passwordParam)

    with open(f"{fileNameParam}.dcr", "w", encoding="utf-8") as fileObject:
        fileObject.write(decryptedContent)

fileName="sample.txt"
encryptedFileName="sample.txt.enc"
command=input("Which process do you want? (E)ncrypt/(D)ecrypt: ").lower()
password=int(input("Enter an encryption key(1-255): "))
if command== "e":
    encryptFile(fileName,password)
elif command== "d":
    decryptFile(encryptedFileName,password)
