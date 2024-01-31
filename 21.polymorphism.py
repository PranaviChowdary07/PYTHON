""" 
  Polymorphism --> The ability of a thing to take on many forms
  -Ex:-
  print(3 + 6)  -->O/P : 9
  print('3' + '6') --> O/P :36
  Strings add --> concatenation

  Types:
  - Duck Typing:- It comes from one phrase i.e "If it looks like a duck & quacks like a duck.It's a duck"
    """ 
class Duck:
    def sound(self):
        print("Quack Quack")

class Dog:
    def sound(self):
        print("Bow Bow")

class Cat:
    def sound(self):
        print("Meaow Meaow")
def anysound(obj):
    obj.sound()

#X = Duck()
X = Cat()
Y = Dog()
anysound(X)