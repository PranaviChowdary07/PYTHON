""" Operator Overloading & Method Overriding """
""" 8 + 4 --> 8,9 are operands,+ is operator """

a = 14
b = 4
print(a + b)
# behind code running
print(int.__add__(a,b))
# For string
a = "Pranavi"
b = "Kasthuri"
print(str.__add__(a,b))

# Example:

class Student:
    def __init__(self,m1,m2) :
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):   # when use the error doesnot occur
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1,m2)   # It converts to object
    def __gt__(self,other):
        s1tm = self.m1 + self.m2
        s2tm = other.m2 + other.m2
        if s1tm > s2tm:
            return True
        else:
            return False

s1  = Student(80,45)
s2  = Student(45,57) # It shows type error: unsupported type for +: "student"
s3 = s1 + s2
# s3 = Student(55 + 56 , 56 + 2)
print(s3.m1 ,s3.m2)
""" if s1 > s2:
    print("s1 Wins")
else:
    print("s2 Wins")
     
      It shows > not supported b/w instaces(obj.s) """
if s1 > s2:
    print('S1 TM : ',s1.m1 + s1.m2)
    print('S2 TM : ',s2.m1 + s2.m2)
    print("s1 Wins")
else:
     print('S1 TM : ',s1.m1 + s1.m2)
     print('S2 TM : ',s2.m1 + s2.m2)
     print("s2 Wins")


     # Method Overriding
class Parent:
    def Bike(self):
        print("I have Passion Pro Bike")

class Child(Parent):
    # pass --> it executes parent
    def Bike(self):
        print("I have Pulsar 220cc Bike")  # --> it shows child
obj1 = Child()
obj1.Bike()
# Method Override: It checks first child property (it executes) when child has no property it executes parent property
