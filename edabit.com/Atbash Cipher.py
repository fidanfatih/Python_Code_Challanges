# https://edabit.com/challenge/MGALfBAXhXqqdFyqo
def atbash ( txt ) :
    ch= ''.join([ chr(65+i) for i in range(58) ]) # ascii kodu 65'ten 123e karakterlerin stringi oluşturur
    return ''.join([ch[::-1] [ch.index(i)] if i.isalpha() else i for i in txt]).swapcase()

    # 'A-Z' nın ascii kodu 65-90 dır. harflerin ascii kodu ardışık gider. 'a-z'nin ascii kodu 97-122 dır.
    # ch = ''.join([ chr(65 + i) for i in range(58) ])
    # out =''
    # for i in txt:
    #     if i.isalpha( ) :
    #         out+=ch[::-1] [ch.index(i)]
    #     else:
    #         out+=i
    # return out.swapcase()

print(atbash("Hello world!"))