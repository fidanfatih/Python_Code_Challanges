def encrypt(stringParam:str,passwordParam:int) ->str:
    encryptedString=""
    for character in stringParam:
        encryptedString+=chr(ord(character)^passwordParam)
    return encryptedString


def decrypt(stringParam:str,passwordParam:int) ->str:
    decryptedString = ""
    for character in stringParam:
        decryptedString += chr(ord(character) ^ passwordParam)
    return decryptedString


password=15
string="La ilahe illallah, Muhammeden resulullah"

encryptedString = encrypt(string,password)
print(f"Encrypted String is '{encryptedString}'")

decryptedString=decrypt(encryptedString,password)
print(f"Decrypted String is '{decryptedString}'")