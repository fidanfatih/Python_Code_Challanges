text=input("cümle giriniz ")
dictionary={
     "this":[("noun","bu,şu")],
     "is":[("verb","olmak")],
     "a":[("adjective","bir")],
     "it":[("adverb","o,onu,ona")],
     "book":[("noun","kitap"),("verb","rezerve etmek")],
     "good":[("adjective","iyi,güzel"),("noun","hayır"),("adverb","oldukça")]
}
a=set(text.split())
for i in a:
    if i in dictionary:
        print(i ,":",dictionary[i])
    else:
        print(i ,": Kelimenin anlamı bulunamadı")