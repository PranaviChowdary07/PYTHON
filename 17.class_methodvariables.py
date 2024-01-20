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
      --> get method
      --> set method
   2.Class Methods

   3.Static method
 """
class Student :
    school = 'SSVHS'
    def __init__(self):
        self.marks1 = 'Marks 1'
        self.marks2 = 'Marks 2'
        self.marks3 = 'Marks 3'
        # Instance methods
        # == GET Methods == Accessors(another name)
    def get_m1(self):
        return self.marks1
    

    def get_m2(self):
        return self.marks2
    

    def get_m3(self):
        return self.marks3
      # == Set Method == Mutators
    def set_m1(self,value):
        self.marks1 = value
    

    def set_m2(self,value):
        self.marks2 = value


    def set_m3(self,value):
        self.marks3 = value
    
    
        

S1 = Student()
S2 = Student() 


S1.set_m1(98)
print(S1.get_m1())

S2.set_m1(96)
print(S2.get_m1())


