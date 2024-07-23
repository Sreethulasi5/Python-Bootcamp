class Employee:
    def __init__(self,name,eid,salary):
        self.name=name
        self.eid=eid
        self.__salary=salary  # __ for private data for attribute
    def get_salary(self):       # public method and data is private
        print( self.__salary)
    def Empdisplay(self):   #public data
        print(self.name,self.eid)
class Company:
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self): # protected data
        print("hirning the freshers")
cobj=Company('wipro','gachibowli')
eobj=Employee('thulasi',309, 86000)
eobj.Empdisplay()
cobj._hiring()
eobj.get_salary()