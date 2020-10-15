#Modül
"""
>> base64 encoding i binary verileri, matematiksel işlemler için kullanılmaz. veriyi metne çevirip kaydedip saklamak
veya başka bir yazılıma göndermek için kullanırız.
>> { A,B,C,D...Z,a,b,c,d....z,0,1,2,3....,9,+,/ } karakterleri (toplam 64 karakter) kullanılır.
>> base64 encoding yapılan dosyalar XML, JASON gibi dosyalarda kaydeidlebilir ve kolayca bir yerden biryere
iletilebilir hale geliyor.
>> base64 e çevireceğimiz verileri normalde binary verilerden seçeriz.
Ancak istersek tüm verileri base64 encoding yapabiliriz.
>> base64 ile her 3 byte veri, 4 byte çevrilir ama veri nihayetinde metin olduğu için bu çok kolaylıklar sağlar.
>> veri 1 veya 2 byte ise kalan byte lar 0 kabul edilir ve yine 4 byte çevrilir.
base64 te (000000) binary değer '=' ile yazılır.
>> "Hak" kelimesinde her harf 1 byte tır ve ASCII kodu ile tutulur. H(72),a(97),k(107)
ASCII kodun karşılığı ise binary değerdir.H(0100 1000),a(0110 0001),k(0110 1011)
Hak kelimesinde toplam 24 bit var(4*6bit)
18(010010) 6(000110) 5(000101) 43(101011)   ASCII tablosuna bakarsak 18=S,6=G,5=F,r=43 olduğunu görürüz.
"Hak" stringinin base64 encodingte karşılığı "SGFr" dir.
"""
def stringToBase64(string:str) ->str:
    stringAsBinary = string.encode("utf-8") #byte type değer döner
    stringAsBase64 = base64.b64encode(stringAsBinary)  #byte type değer döner, bu fonksiyon içinde byte array olmalıdır.
    string = stringAsBase64.decode("utf-8") #str değer döner
    return string


def base64ToString(string:str) ->str:
    stringAsBase64 = string.encode("utf-8") #byte type değer döner
    stringAsBinary= base64.b64decode(stringAsBase64) #byte type değer döner
    string = stringAsBinary.decode("utf-8") #str değer döner
    return string


def numberToBase64(number:int) ->bytes:
    # numberAsBit=bin(number)[2:]   #bin string döndürür
    numberOfByte=ceil(int(log(number,2)+1)/8)
    numberAsByte=number.to_bytes(numberOfByte,byteorder="little") #byte type değer döner
    numberAsBase64=base64.b64encode(numberAsByte) #byte tipinde değer döner
    string=numberAsBase64.decode("utf-8") #str değer döner
    return string

def base64ToNumber(string:str) ->int:
    string=string.encode("utf-8") #bytes tipinde değer döner
    numberAsBytes=base64.b64decode(string)  #bytes tipinde değer döner
    number=int.from_bytes(numberAsBytes,byteorder="little") #int tipinde değer döner
    return number


import base64
from math import log,ceil
