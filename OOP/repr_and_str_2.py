class employee :
    salary_increase_coefficient = 1.05
    stuff_num = 0

    def __init__ (self , name , surname , salary) :
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = (self.name + self.surname).lower ( ) + "@sirket.com"
        employee.stuff_num += 1

    def fullName (self) :
        return f"Ad:{self.name} Soyad:{self.surname}"

    def salary_hike (self) :
        self.salary *= self.salary_increase_coefficient

    def __str__(self):
        return f"{self.fullName()} e-mail:{self.email}"

    def __repr__(self):
        return f'employee ({self.name}, {self.surname}, {self.email})'


personal1 = employee ( "Fatih" , "Fidan" , 5000 )
personal2 = employee ( "Serap" , "Çelik" , 4000 )
print(personal1)
# normalde bu ifade nesnenin adresini dönderecek iken __str__ yeniden tanımlanarak yazdırabiliyoruz.

print(repr(personal2))
# normalde bu ifade nesnenin adresini dönderecek iken __repr__ yeniden tanımlanarak yazdırabiliyoruz.
# repl fonksiyonunda geleneksel olarak classın özelliğini,adını vs bir şekilde içeremelidir. bu onun str den farkıdır.