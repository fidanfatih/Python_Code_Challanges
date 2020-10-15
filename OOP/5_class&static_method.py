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

    @classmethod
    def change_salary_inc_coef (cls , new_rate) :
        cls.salary_increase_coefficient = new_rate

    @classmethod
    def new_staff(cls,stuff_info):
        name,surname,salary=stuff_info.split("-")
        return cls(name,surname,int(salary))

    @staticmethod
    def clear_blank(text):
        return text.replace(" ","")

personal1 = employee ( "Fatih" , "Fidan" , 5000 )
personal2 = employee ( "Serap" , "Çelik" , 4000 )

employee.salary_increase_coefficient=1.5
# veya
# employee.change_salary_inc_coef(1.5)

mpersonel1="    Ali- Candan-6000"
mpersonel2="Polat-Alemdar-4500"
mpersonel1=employee.clear_blank(mpersonel1)

new_personel1=employee.new_staff(mpersonel1)
new_personel1.salary_hike()
print(f"{new_personel1.name} {new_personel1.surname} {new_personel1.salary} {new_personel1.email}")

"""
class metodlar nesne üreten nesnedir. 
mesela bir arayüzde bir butona basınca başka butonların üretilmesini istiyorsak
class metod kullanırız.
class metodlar çalışınca class içindeki variable lar ve instance metodların üretiği değer etkilenir.

static metod çalışmasından class içindeki diğer metodlar etkilenmez, bağımsız çalışır,
static metod, class metod içinden veya instance metod içinden de çağırılabilir.
"""




