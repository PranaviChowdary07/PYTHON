""" 
  Polymorphism --> The ability of a thing to take on many forms
  -Ex:-
  print(3 + 6)  -->O/P : 9
  print('3' + '6') --> O/P :36
  Strings add --> concatenation

  Types:
  - Duck Typing:- It comes from one phrase i.e "If it looks like a duck & quacks like a duck.It's a duck"
  -- similar methods to do duck typing
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

# Example :- 2

class India:
    def capital(self):
        print("New Delhi")

    def lang(self):
        print("Hindi")

class USA:
    def capital(self):
        print("Washington, D.C.")
    def lang(self):
        print("English")

def caplan(obj):
    obj.capital()
    obj.lang()

a = USA()
caplan(a)







