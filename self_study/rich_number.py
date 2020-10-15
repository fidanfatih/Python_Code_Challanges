# https://www.matematikciler.com/zengin-sayi/

n=3
while True:
    if sum([i for i in range(1,n//2+1) if not n%i])>n and n%2:print(n);break
    n+=1