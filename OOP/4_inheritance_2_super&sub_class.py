class employee ():                      # super class
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
    def new_staff (cls , stuff_info) :
        name , surname , salary = stuff_info.split ( "-" )
        return cls ( name , surname , int ( salary ) )

    @staticmethod
    def clear_blank (text) :
        return text.replace ( " " , "" )


class developer ( employee ) :                      # sub class
    def __init__ ( self , name , surname , salary , p_len ) :
        # employee.__init__(name,surname,salary)  # veya
        super ( ).__init__ ( name , surname , salary )
        self.p_len = p_len
        self.salary_increase_coefficient= 1.2


class manager (employee):                             # sub class
    def __init__(self,name,surname,salary,staff=None):
        super().__init__(name,surname,salary)
        if staff is None:
            self.staff=[]
        else:
            self.staff=staff

    def add_staff_member( self, staff_member ):
        self.staff.append(staff_member)

    def remove_staff_member( self, staff_member ):
        self.staff.remove(staff_member)

    def list_staff( self ):
        for staff_member in self.staff:
            print(staff_member.fullName())


personal1 = employee( "Fatih" , "Fidan" , 5000 )
personal2 = employee( "Serap" , "Çelik" , 4000 )

developer1 = developer ( "Bill" , "Gates" ,7000, "Python" )
print(developer1.fullName(), developer1.p_len, developer1.salary)
developer1.salary_hike ( )
print(developer1.salary)

manager1 = manager ( "Steve" , "Jobs" , 10000 , [ developer1 , personal1 ] )
print ( manager1.fullName ( ) )
print()
manager1.list_staff ( )
print()
manager1.add_staff_member ( personal2 )
manager1.list_staff ( )
print()
manager1.remove_staff_member ( developer1 )
manager1.list_staff ( )
