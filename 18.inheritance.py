""" 
Inheritance :- class methods and properties used in another class .

 -- Types :-

        1.Single Inheritance
           - One parent class,one child class
        2.Multiple Inheritance
           - Multiple parent classes ,child class(accept multiple parent class)

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
obj.fun2() # --> O/P = Child

# Multiple Inheritace

class Mother:
    mother_name = ""
    def mom(self):
        print(self.mother_name)

class Father:
     father_name =""
     def dad(self):
         print(self.father_name)

class Son(Mother,Father):
    son_name = ""
    def shownames(self):
        print(self.son_name," Son of Mr & Mrs",self.father_name ,'-',self.mother_name)

obj = Son()
obj.father_name = "Arjun"
obj.mother_name = "Sneha"
obj.son_name = "Ayan"
obj.shownames()
