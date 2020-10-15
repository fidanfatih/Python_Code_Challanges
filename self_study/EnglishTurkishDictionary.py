dictionary={
     "this":[("noun","bu,şu")],
     "is":[("verb","olmak")],
     "a":[("adjective","bir")],
     "it":[("adverb","o,onu,ona")],
     "book":[("noun","kitap"),("verb","rezerve etmek")],
     "good":[("adjective","iyi,güzel"),("noun","hayır"),("adverb","oldukça")]
}
wordDefinitions=set()
punctuation=".,:;!'?%=()[]{}/\*+-"+'"'
maxLenghtOfWord=0

while True:
    sentences=input("\nBir cümle giriniz(Çıkış için 'ENTER' a basınız!): ")
    if sentences=="":
        break
    for sign in punctuation:
        if sign in sentences:
            sentences=sentences.replace(sign,'')

    words=set(sentences.lower().split())
    for word in words:
        if len(word)>maxLenghtOfWord:
            maxLenghtOfWord=len(word)

    for word in words:
        wordDefinitions=dictionary.get(word,"[ANLAMI BULUNAMADI]")
        if wordDefinitions=="[ANLAMI BULUNAMADI]":
            print(f"[{word.upper():<{maxLenghtOfWord}}] :{wordDefinitions}")
        elif len(wordDefinitions)>0:
            print(f"[{word.upper():<{maxLenghtOfWord}}] :",end="")
            for wordDefinition in wordDefinitions:
                print(f"({wordDefinition[0]:^9}){wordDefinition[1]} ",end="")
            print()
    maxLenghtOfWord=0
    print()
print("\nProgramdan çıktınız...")