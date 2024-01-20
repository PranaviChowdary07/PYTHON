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
    def __init__(self) :
        self.model =  'model'
        self.ram = 'ram'
        self.rom = 'rom'
        self.color = 'color'
 
    def info(self):
        print('VIVO',self.model,'info :')
        print('Model -',self.model)
        print('RAM   -',self.ram)
        print('ROM   -',self.rom)
        print('COLOR -',self.color)
        print(' ')
mob1 = VivoMobile()
mob1.model = 'V20'
mob1.ram = '8GB'
mob1.rom = '64GB'
mob1.color = 'Blue'
mob1.info()

mob2 = VivoMobile()
mob2.model = 'X50'
mob2.ram = '16GB'
mob2.rom = '128GB'
mob2.color = 'Black'
mob2.info()

mob3 = VivoMobile()
mob3.model = 'Y15'
mob3.ram = '16GB'
mob3.rom = '256GB'
mob3.color = 'White'
mob3.info()

