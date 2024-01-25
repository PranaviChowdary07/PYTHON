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


# Single Inheritance

class Parent:

    def fun1(self):
        print("Parent")

class Child(Parent):
    def fun2(self):
        print("Child")

obj = Child()
obj.fun1() # --> O/P = Parent
obj.fun2() # -- > O/P = Child