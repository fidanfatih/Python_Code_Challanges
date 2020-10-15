# https://www.matematikciler.com/uc-asal-sayi/
def is_prime(n):
    return n==2 or all([n%i for i in range(2,int(n**0.5)+1)]) and n not in [0,1]

def search():
    for i in range (11,100,2):
        for j in range(11,100,2):
            for k in range(11,100,2):
                list1=[is_prime((i+j+k)//3),is_prime((i+j)//2),is_prime((k+j)//2),is_prime((i+k)//2),is_prime(i),is_prime(j),is_prime(k)]
                list2=[(i+j+j)%3,(i+j)%2,(k+j)%2,(i+k)%2]
                list3=[i!=j,i!=k,j!=k]
                if all(list3) and not any(list2) and all(list1):
                    return [i,j,k]
    return []

print(search())
