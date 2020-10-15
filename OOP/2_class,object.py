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


personal1 = employee ( "Fatih" , "Fidan" , 5000 )
personal2 = employee ( "Serap" , "Çelik" , 4000 )

print ( personal1.name , personal1.surname , personal1.salary )
employee.salary_hike ( personal1 )
print ( personal1.name , personal1.surname , personal1.salary )

personal2.salary_increase_coefficient = 1.1         # class variable'ı personel2 için değiştirebiliriz.
# personal2.salary_hike ( ) # veya
employee.salary_hike ( personal2 )
print ( personal2.name , personal2.surname , personal2.salary )

print( f"Personel Sayısı: {employee.stuff_num}")  #init metodu içinden tanımlanan obje sayısını izleyebiliriz.
