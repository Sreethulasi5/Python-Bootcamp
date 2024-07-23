# abstraction using mobiles example
from abc import ABC
class Mobile(ABC):
    def price():# different for every phone(abstract)
        pass
    def text():# which are common(non-abstraction)
         print('texting is similar for all phones')
    def calling():
        print('it provides calling fecilities')
class Vivo(Mobile):
    def camera():
        print('camera quality is best')
class Motorola(Mobile):
    def waterproof():
        print('mobile is waterproof')
vobj=Vivo
vobj.camera()
vobj.price()
vobj.text()
mobj=Motorola
mobj.waterproof()