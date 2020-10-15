#dosyadan binary değerleri al, terminale karakter karakter hex karşılıklarıyla yazdır.
def bytesFromFile(fileName):
    try:
        with open(fileName,"rb") as fileObject:
            while True:
                chunk=fileObject.read()
                if chunk:
                    for byteInChunk in chunk:
                        yield byteInChunk  #yield, return gibi ama devamlı surette kaldığı yerden değer döndürür.
                else:
                    break
    except:
        return


for byte in bytesFromFile("deneme2.txt"):
    print(f"{chr(byte)}:{byte:X}")



