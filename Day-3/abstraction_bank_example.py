# abstraction using bank example
from abc import ABC
class RBIBank(ABC):
    def interest():
        pass
    def loan():
        print("home lone")

class HDFC(RBIBank):
    def interest():
        print("7.5 per interest")
class SBI(RBIBank):
    def interest():
        print("11per per interest")
class AXIS(RBIBank):
    def interest():
        print("7.5 per interest")
obj=HDFC
obj.interest()
ob=HDFC
ob.loan()
obj1=SBI
obj1.interest()
obj2=RBIBank    
obj2.interest()
