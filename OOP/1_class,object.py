class employee:
    salary_increase_coefficient=1.05
    def __init__(self,name,surname,salary):
        self.ad=name
        self.soyad=surname
        self.maaş=salary
        self.eposta=(self.ad+self.soyad).lower()+"@sirket.com"

    def fullName(self):
        return f"Ad:{self.ad} Soyad:{self.soyad}"


personal1=employee("Fatih","Fidan","5000")
personal2=employee("Serap","Çelik","4000")

print(personal1)
print(personal1.ad,personal1.soyad,personal1.eposta)

print(personal1.fullName())

print(personal2.fullName()) # veya
print(employee.fullName(personal2))

print(employee.salary_increase_coefficient) # veya
print(personal1.salary_increase_coefficient)
print(personal2.salary_increase_coefficient)
