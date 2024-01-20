                    # Type of Variables in Class
""" 
 Class Variables are two types :-
    1.Class or Static 
      --> no change
    2.Instance -->used in def function
      --> it instnace changes to every obj
 """

# Example
class Bike :
    # Class/Static Variable
    tyres = 2
    def __init__(self) :
        # Instance Variable
        self.name ="Bike Name"
        self.year = '2020'
        self.color = 'Blue'
bike1 = Bike()
bike1.name = 'Activa 60'
bike1.year = '2021'
bike1.color = 'Black'
print(bike1.name,bike1.year,bike1.color,Bike.tyres)

bike2 = Bike()
bike2.name = 'Bullet'
bike2.year = '2000'
bike2.color = 'Green'
print(bike2.name,bike2.year,bike2.color,Bike.tyres)

                      #  Types of Methods in Class
""" 
   1.Instance Methods

   2.Class Methods

   3.Static method
 """
class Student :
    school = 'SSVHS'
    def __init__(self):
        self.marks1 = 'Marks 1'
        self.marks2 = 'Marks 2'
        self.marks3 = 'Marks 3'

S1 = Student()
S2 = Student() 

