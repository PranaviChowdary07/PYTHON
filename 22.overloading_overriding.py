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

s1  = Student(23,45)
s2  = Student(45,57) # It shows type error: unsupported type for +: "student"
s3 = s1 + s2
# s3 = Student(55 + 56 , 56 + 2)
print(s3.m1 ,s3.m2)
