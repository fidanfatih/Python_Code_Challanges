# def encrypt(w):
#     d={"a":"0","e":"1","i":"2","o":"2","u":"3"}
#     return ''.join([i*(d.get(i)==None) or d[i] for i in w][::-1])+"aca"

# def encrypt(word):
# 	B = word[::-1]
# 	C=B.maketrans({ord('a'): ord('0'),ord('e'): ord('1'),ord('o'): ord('2'),ord('u'):ord('3')})
# 	return B.translate(C)+'aca'

# def encrypt(word):
# 	b=word[::-1]
# 	c=b.replace("a","0").replace("e","1").replace("i","2").replace("o","2").replace("u","3")
# 	return c + "aca"

encrypt=lambda w:w.translate(w.maketrans("aeiou","01223"))[::-1]+"aca"
print(encrypt("karaca"))