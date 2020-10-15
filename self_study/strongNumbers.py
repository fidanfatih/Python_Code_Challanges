# Strong Number, basamak değerlerinin faktoriyel leri Toplamı kendine eşit olan sayıya denir
# İlk 4 Strong Numbers listesini döndüren fonksiyonu yazabiliriz.
# https://www.w3resource.com/c-programming-exercises/for-loop/c-for-loop-exercises-47.php
from math import factorial as f
def is_strong(n):
    return sum((f(int(i)) for i in str(n)))==n

def strong():
    nums,n=[],1
    while len(nums)<4:
        if is_strong( n ): nums.append( n )
        n+=1
    return nums

print(strong())