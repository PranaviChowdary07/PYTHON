""" 
Inheritance :- class methods and properties used in another class .

 -- Types :-

        1.Single Inheritance
           - One parent class,one child class

 """

 # Example 
class A:   # Parent Class Or Base Class
    x = "Something"

class B(A):  # Child Class or Derived Class
    y = "Nothing"

obj = A()
print(obj.x)