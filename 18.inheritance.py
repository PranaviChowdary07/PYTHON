""" 
Inheritance :- class methods and properties used in another class .

 -- Types :-

        1.Single Inheritance
           - One parent class,one child class
        2.Multiple Inheritance
           - Multiple parent classes ,child class(accept multiple parent class)
           - One sub class having multiple parents
        3.Multi-level Inheritance
          - Parent class
          - Intermediate class
          - derived class
          - A -> B -> C
        4.Hierarchical Inheritance
          - One parent multiple subclasses
          - Ex:-
          A-->parent class
          B(A)
          C(A)
          D(A)
        5.Hybrid Inheritance
          - Combination of atleast two inheritance types

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

# Multi-level Inheritance

class Mango:
    def func1(self):
        print("From Mango")

class Apple(Mango):
    def func2(self):
        print("From Apple")

class Orange(Apple):
    def func3(self):
        print("From Orange")

fruits = Orange()
fruits.func1()
fruits.func2()
fruits.func3()

# Hierarchical Inheritance
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meaow")

dog = Dog()
dog.speak()

cat = Cat()
cat.speak()

# Hybrid Inheritance
 
class Vehicle:
    def start(self):
        print("Vehicle Starts....")
class ElectricVehicle(Vehicle):       # Single
    def charge(self):
        print("Charging......")
class Car(Vehicle):               # Hierchical 
    def drive(self):
        print("Drives the car")
class HybridCar(Car,ElectricVehicle):   # Multiple
    def fuel(self):
        print("Starting with a combination of fuel & electric")

hybridCar = HybridCar()
hybridCar.charge()
hybridCar.drive()
hybridCar.fuel()
hybridCar.start()