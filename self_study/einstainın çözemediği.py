# Hadi Einstein'a biraz yarsımcı olalım...
# https://www.matematikciler.com/einsteinin-cozemedigi-soru/
def eggs():
    i=100
    while True:
        if not any((i%2,i%3,i%4,i%5,i%6,i%7,i%8,i%9,i%10,(i+1)%11)): break
        i+=10
    return i+1

print(eggs())