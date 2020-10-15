# EBOB, EKOK
# Kullanıcının girdiği iki sayının ebob ve ekokunu bulan program yazalım. Bugün fonksiyonlara geçiş yapacağız. Soruyu fonksiyon kullanarak yapabiliriz.

def ebob(n1,n2):
    for i in range(n1,0,-1):
        if not(n2%i or n1%i): return i

def ekok(n1,n2):
    for i in range (n2,n1*n2+1):
        if not(i%n2 or i%n1): return i

nums=[int(input(f"Number{i+1}: ")) for i in range(2)]
print(f"EBOB{nums} = {ebob(min(nums),max(nums))}\n"
      f"EKOK{nums} = {ekok(min(nums),max(nums))}")
