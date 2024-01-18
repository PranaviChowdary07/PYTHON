# Class -->like blueprint
""" 
class --> class name must be start with Capital letter
Obj --> attributes/properties(data) & behaviour/methods(action)
Bike -->engine,color,speed & 1st gear

class VivoMobile:
    x = 34
    def samplemethod(self):
        print(self.x)


obj1 = VivoMobile()
obj1.samplemethod()  # Another way cal method
VivoMobile.samplemethod(obj1)  # // (self = obj1) """

class VivoMobile:
    def __init__(self,model,ram,rom,color) :
        self.model =  model
        self.ram = ram
        self.rom = rom
        self.color = color
        
    def info(self):
        print(self.model,self.ram,self.rom,self.color)
        print(' ')
mob1 = VivoMobile('x12','12GB','8GB','Blue')
mob1.info()

mob2 = VivoMobile('Z13','64Gb','16GB','Red')
mob2.info()

