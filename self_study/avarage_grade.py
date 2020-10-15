# Write a Python code that calculates the average of scores that students took in a math class at below.

def avg_grade(**kwargs):
    name = [ ]
    age = [ ]
    for key , value in kwargs.items ( ):
        name.append ( key )
        age.append ( value )
    print("Avarage grade: ",sum(age)/len(age))


scores = {
    "Mary" : 85,
    "Susan": 75,
    "Barry" : 65,
    "Alexis" : 88,
    "Jane" : 45,
    "Tina" : 100,
    "Tom" : 90,
    "Tim": 60
}

avg_grade(**scores)