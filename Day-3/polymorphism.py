class Person():
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def __str__(self):
        return f'{self.name} {self.age} {self.height}'
class Student(Person):
    def __init__(self,name,age,height,roll,branch):
        super().__init__(name,age,height)
        self.roll=roll
        self.branch=branch
    def __str__(self):
        perdetails=super().__str__()
        return f'{perdetails}{self.roll} {self.branch}'
class Annualday(Student):
    def __init__(self,name,age,height,roll,branch,program):
        super().__init__(name,age,height,roll,branch)
        self.program=program
    def __str__(self):
        studetails=super().__str__()
        return f'{studetails} {self.program}'
aobj=Annualday('Thulasi',20 ,5 ,23,'CSE','solo')
print(aobj)




